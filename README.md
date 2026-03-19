# **Reto Técnico: AI Engineer**
## **LLM IntelliAgent – Service Desk Assistant**

---

## **Descripción**

Este proyecto implementa un asistente inteligente para Service Desk basado en LLMs que:
- Clasifica automáticamente tickets (severidad + área)
- Responde preguntas sobre tickets históricos mediante RAG
- Proporciona trazabilidad citando tickets relevantes
- El sistema está diseñado como un prototipo funcional (POC) con una arquitectura modular, simple y escalable.

---

## **Objetivos**
* Clasifica tickets automáticamente (LLM + prompt engineering)
* Implementa un RAG con PostgreSQL + pgvector
* Permite consultas sobre tickets históricos
* Mantiene arquitectura simple pero escalable

---

## **Arquitectura**

                ┌──────────────────────┐
                │      Usuario         │
                │   (Streamlit UI)     │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │       app.py         │
                │    Orquestador       │
                └─────────┬────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐

│ classifier   │    │     rag      │    │ embeddings   │

│ (LLM)        │    │(RAG pipeline)│    │ ingestion    │

└──────┬───────┘  └──────┬───────┘  └──────┬───────┘

       │                 │                 │

       ▼                 ▼                 ▼

   OpenAI API         FAISS Index          PostgreSQL

                    (vector search)        (storage)


---

## **Stack Tecnológico**

| Componente    | Tecnología                        |
| ------------- | --------------------------------- |
| LLM           | OpenAI (`gpt-4o-mini`)            |
| Embeddings    | OpenAI (`text-embedding-3-small`) |
| Vector Search | FAISS                             |
| Base de datos | PostgreSQL                        |
| UI            | Streamlit                         |
| Lenguaje      | Python                            |


---

## **Caracteristicas**

Componentes clave
1. LLM Layer (OpenAI API)
- Clasificación → gpt-4o-mini (rápido + barato)
- Generación RAG → gpt-4o-mini o gpt-4.1

2. Vector Store: PostgreSQL + FAISS
- PostgreSQL = persistencia (tickets + metadata)
- FAISS = búsqueda semántica (embeddings)
- LLM = clasificación + generación de respuestas
- Permite búsqueda vectorial eficiente en memoria
- Ideal para prototipos y datasets pequeños

3. Embeddings
- text-embedding-3-small = Balance óptimo entre costo y rendimiento

4. Pipeline RAG

                [Pregunta usuario]

                        ↓

                [Generar embedding]

                        ↓

                [FAISS - búsqueda vectorial]

                        ↓

                [Top-K tickets relevantes]

                        ↓

                [Construcción de contexto]

                        ↓

                [LLM genera respuesta]

                        ↓

                [Respuesta con JSon]

      

---

## **Estructura del Proyecto**

llm-intelliagent/

│

├── README.md

├── requirements.txt

├── .env

│

├── data/

│   └── tickets.csv

│

├── prompts/

│   ├── classifier_prompt.txt

│   └── rag_prompt.txt

│

├── src/

│   ├── config.py

│   ├── db.py

│   ├── classifier.py

│   ├── embeddings.py

│   ├── rag.py

│   └── app.py

│

└── docs/

    └── decisiones.md


---

## **Instalación del Prooyecto**

1. Clonar repositorio

    git clone  https://github.com/maluramos72/llm-intelliagent.git

    cd llm-intelliagent

2. Crear entorno virtual

python -m venv venv

venv\Scripts\activate

3. Instalar dependencias

pip install -r requirements.txt

4. Configurar variables de entorno

Crear archivo .env:

OPENAI_API_KEY=your_api_key

DB_HOST=localhost

DB_PORT=5432

DB_NAME=llm_agent

DB_USER=postgres

DB_PASSWORD=postgres


7. Ejecutar aplicación

streamlit run src/app.py

