import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt():
    with open("prompts/classifier_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def classify_ticket(text):
    prompt_template = load_prompt()
    prompt = prompt_template.replace("{{ticket}}", text)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content