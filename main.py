import streamlit as st
from qa_pipeline import ingest_document, ask_question

st.title("AI Assistant for Kazakhstan's Constitution")

uploaded_files = st.file_uploader("Upload PDF/Text files", type=["pdf", "txt"], accept_multiple_files=True)

with open("constitution/kz_constitution.txt", "r", encoding="utf-8") as f:
    text = f.read()
    ingest_document(text, source="Kazakhstan Constitution")

query = st.text_input("Ask a question about the Constitution or uploaded documents")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        answer = ask_question(query)
        st.write("💬 **Answer:**")
        st.success(answer)
