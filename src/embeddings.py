import faiss
import numpy as np
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
from db import engine
from sqlalchemy import text

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# FAISS index
index = faiss.IndexFlatL2(1536)
documents = []

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def ingest_csv(path="data/tickets.csv"):
    df = pd.read_csv(path)

    with engine.connect() as conn:
        for _, row in df.iterrows():
            emb = get_embedding(row["descripcion"])

            # guardar en postgres (sin embedding)
            conn.execute(text("""
                INSERT INTO tickets (ticket_id, descripcion, metadata)
                VALUES (:id, :desc, :meta)
                ON CONFLICT (ticket_id) DO NOTHING
            """), {
                "id": row["ticket_id"],
                "desc": row["descripcion"],
                "meta": row.to_json()
            })

            # guardar en FAISS
            index.add(np.array([emb]).astype("float32"))

            documents.append({
                "id": row["ticket_id"],
                "descripcion": row["descripcion"]
            })