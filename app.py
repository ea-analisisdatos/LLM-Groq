import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("groq_api_key")

st.sidebar.title("🛠️ **Personalización**")
prompt = st.sidebar.title("Modelos: ")
model = st.sidebar.selectbox(
    'Choose a model', ['Llama3-8b-8192', 'Llama3-70b-8192', 'Mixtral-8x7b-32768']
)

# Groq client
client = Groq(api_key = groq_api_key)

# Streamlit Interface
st.title("💬 Chat con LLM de Groq")

# Initialize sessesion state for history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("**Ingresa tu consulta**: ", "")

if st.button("Enviar"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content" : user_input,
            }
        ],
        model = model,
    )
    # Store the query and response in history
    response = chat_completion.choices[0].message.content
    st.session_state.history.append({"query" : user_input, "response" : response})

    # Display the response
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

# Display history
st.sidebar.title("Historial")
for i, entry in enumerate(st.session_state.history):
    if st.sidebar.button(f'Query {i+1}: {entry["query"]}'):
        st.markdown(f'<div class="response-box">{entry["response"]}</div>', unsafe_allow_html=True)
        