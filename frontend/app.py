import streamlit as st
import requests

st.set_page_config(page_title="AI Text Summarizer", layout="centered")

st.title("🧠 AI Text Summarizer")

st.write("Paste your text below and click summarize")

user_input = st.text_area("Enter your text here:", height=200)

if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        with st.spinner("Generating summary..."):
            response = requests.post(
                "http://localhost:8000/summarize/",
                 json={"text": user_input}
            )

            summary = response.json().get("summary", "Error")

            st.subheader("Summary:")
            st.success(summary)

            