import os
from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " "]
)

PERSIST_DIR = "./chroma_db"

vectorstore = None

def ingest_document(text, source="Uploaded File"):
    global vectorstore
    text = text.lower()

    docs = splitter.create_documents([text], metadatas=[{"source": source}])
    print(f"📄 Ingested {len(docs)} chunks from {source}")

    if os.path.exists(PERSIST_DIR):
        vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embedding)
        vectorstore.add_documents(docs)
    else:
        vectorstore = Chroma.from_documents(docs, embedding=embedding, persist_directory=PERSIST_DIR)

    vectorstore.persist()
    print("✅ Vector store saved to disk.")

def ask_question(query):
    global vectorstore

    if vectorstore is None:
        print("❌ Vector store is not initialized.")
        return "I don't have any documents to answer from."

    query = query.lower()

    relevant_docs = vectorstore.similarity_search(query, k=4)

    if not relevant_docs:
        print("⚠️ No relevant documents found for query.")
        return "I couldn't find anything relevant in the Constitution."

    print("\n🔍 Retrieved Chunks:")
    for i, doc in enumerate(relevant_docs):
        print(f"\n--- Chunk {i+1} ---\n{doc.page_content[:500]}...\n")

    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    prompt = f"""
You are an expert on the Constitution of the Republic of Kazakhstan.
Only use the following context to answer the question.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question: {query}
"""
    llm = OllamaLLM(model="mistral")  # Or llama3, gemma, etc.
    return llm.invoke(prompt.strip())
