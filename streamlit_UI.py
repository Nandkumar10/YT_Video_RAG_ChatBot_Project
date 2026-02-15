import streamlit as st
from src.main import ask_video


st.set_page_config(page_title="YouTube RAG Bot")

st.title(" YouTube Video Chatbot")


youtube_url = st.text_input("Paste YouTube link")
question = st.text_input("Ask your question")


if st.button("Ask"):

    if youtube_url and question:

        with st.spinner("Thinking... "):
            answer = ask_video(youtube_url, question)
            st.write(answer)

    else:
        st.warning("Please enter both fields")
