# Decisiones Tecnicas

## 1. Uso de FAISS en lugar de pgvector

Se optó por FAISS debido a:

- Complejidad de instalación de pgvector en Windows
- Necesidad de un entorno rápido para prototipado
- Bajo volumen de datos (no requiere vector DB distribuida)

FAISS permite búsquedas vectoriales eficientes en memoria.

---

## 2. Uso de OpenAI API

Se utilizó OpenAI para:

- Generación de embeddings
- Clasificación de tickets
- Generación de respuestas (RAG)

Motivo:

- Alta calidad sin necesidad de fine-tuning
- Reducción de complejidad de implementación

---

## 3. Separación de responsabilidades

Arquitectura desacoplada:

- PostgreSQL → almacenamiento
- FAISS → búsqueda semántica
- LLM → razonamiento

Esto permite escalar o reemplazar componentes fácilmente.

---

## 4. No uso de fine-tuning

Se evitó fine-tuning porque:

- El problema se resuelve eficientemente con prompting
- Menor costo y complejidad
- Mayor flexibilidad

---

## 5. RAG en lugar de solo LLM

Se implementó RAG para:

- Evitar alucinaciones
- Responder con datos reales
- Mantener trazabilidad

---

## 6. Limitaciones conocidas

- FAISS no persistente
- Dependencia de API externa
- Dataset limitado

---

## 7. Posibles mejoras

- Persistencia de FAISS
- Hybrid search
- Evaluación automática del sistema
- Migración a pgvector o vector DB