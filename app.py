import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("groq_api_key")

# Streamlit Sidebar for Personalization
st.sidebar.title("🛠️ **Personalización**")
if not groq_api_key:
    st.sidebar.subheader("Configura tu API Key de Groq")
    groq_api_key = st.sidebar.text_input(
        "**Ingresa tu API Key para continuar**:",
        type="password",
        placeholder="Tu API Key de Groq aquí",
    )

if not groq_api_key:
    st.warning("⚠️ La API Key es obligatoria para usar esta aplicación.")
    st.stop()  # Detiene la ejecución si no hay una API Key

# Crear cliente Groq con la API Key (ya sea desde .env o ingresada por el usuario)
try:
    client = Groq(api_key=groq_api_key)

    st.sidebar.title("Modelos:")
    model = st.sidebar.selectbox(
        "Elige un modelo", ["Llama3-8b-8192", "Llama3-70b-8192", "Mixtral-8x7b-32768"]
    )

    # Streamlit Interface
    st.title("💬 Chat con LLM de Groq")

    # Initialize session state for history
    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("**Ingresa tu consulta**: ", "")

    if st.button("Enviar") and user_input.strip():
        try:
            # Realizar la consulta al modelo
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model=model,
            )
            # Guardar la consulta y la respuesta en el historial
            response = chat_completion.choices[0].message.content
            st.session_state.history.append({"query": user_input, "response": response})

            # Mostrar la respuesta
            st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ Error al procesar la consulta: {e}")

    # Display history
    st.sidebar.title("Historial")
    for i, entry in enumerate(st.session_state.history):
        if st.sidebar.button(f'Query {i+1}: {entry["query"]}'):
            st.markdown(f'<div class="response-box">{entry["response"]}</div>', unsafe_allow_html=True)

except Exception as e:
    st.error(f"⚠️ Error al inicializar el cliente de Groq: {e}")
