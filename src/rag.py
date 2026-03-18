from openai import OpenAI
from dotenv import load_dotenv
import os
import numpy as np
from embeddings import index, documents, get_embedding

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_similar(query_embedding, k=5):
    D, I = index.search(
        np.array([query_embedding]).astype("float32"), k
    )

    return [documents[i] for i in I[0]]

def load_prompt():
    with open("prompts/rag_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def answer_question(question, embedding_fn):
    query_emb = embedding_fn(question)
    docs = search_similar(query_emb)

    context = "\n\n".join([
        f"Ticket {d['id']}: {d['descripcion']}"
        for d in docs
    ])

    prompt_template = load_prompt()
    prompt = prompt_template \
        .replace("{{context}}", context) \
        .replace("{{question}}", question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content