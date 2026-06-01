import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.write(f"**{msg['role']}**: {msg['content']}")

user_input = st.text_input("메시지 입력")

if st.button("전송"):
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input
    )

    reply = response.output_text

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.rerun()

if st.button("Clear"):
    st.session_state.messages = []
    st.rerun()