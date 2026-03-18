from sqlalchemy import create_engine, text
from config import Config

engine = create_engine(Config.DB_URL)

def init_db():
    with engine.connect() as conn:
   #     conn.execute(text("""
   #     CREATE EXTENSION IF NOT EXISTS vector;
   #     """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            descripcion TEXT,
            metadata JSONB
        );
        """))