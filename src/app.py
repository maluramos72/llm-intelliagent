import streamlit as st
from classifier import classify_ticket
from rag import answer_question
from embeddings import get_embedding

st.set_page_config(page_title="LLM IntelliAgent", layout="wide")

st.title("LLM IntelliAgent - Service Desk")

# Sidebar
option = st.sidebar.selectbox(
    "Selecciona una función",
    ["Clasificador de Tickets", "Consultas RAG"]
)


# CLASIFICADOR
if option == "Clasificador de Tickets":
    st.header("* Clasificador de Tickets")

    description = st.text_area(
        "Describe el problema:",
        height=150,
        placeholder="Ej: El sistema de pagos está caído..."
    )

    if st.button("Clasificar"):
        if description.strip() == "":
            st.warning("Por favor ingresa una descripción")
        else:
            with st.spinner("Clasificando..."):
                result = classify_ticket(description)

            st.subheader("Resultado:")
            st.code(result, language="json")



# RAG
elif option == "Consultas RAG":
    st.header("* Asistente de Consultas")

    question = st.text_input(
        "Haz una pregunta:",
        placeholder="Ej: ¿Cuántos tickets críticos hubo?"
    )

    if st.button("Consultar"):
        if question.strip() == "":
            st.warning("Por favor escribe una pregunta")
        else:
            with st.spinner("Buscando respuesta..."):
                answer = answer_question(question, get_embedding)

            st.subheader("Respuesta:")
            st.write(answer)