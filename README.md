# ai-constitution-assistant

An AI-powered chatbot that answers questions about the Constitution of Kazakhstan using RAG (Retrieval-Augmented Generation) with:
Streamlit (web interface)
ChromaDB (vector database for constitutional texts)
Ollama (local LLM like Llama 3/Mistral for answers)

# Setup

Prerequisites:

Python 3.10+
Ollama installed (run ollama pull llama3 or mistral)
ChromaDB (pip install chromadb)

Installation:

git clone https://github.com/abdaber/ai-constitution-assistant.git  
cd ai-constitution-assistant
pip install -r requirements.txt

Run Locally:

streamlit run app.py

Project Structure:

├── main.py                  # Streamlit frontend  
├── qa_pipeline.py           # RAG pipeline (ChromaDB + Ollama)  
├── constitution/  
│   └── kz_constitution.txt  # Constitution text
├── requirements.txt         # Python dependencies  
└── README.md  

## Demo 
![image](https://github.com/user-attachments/assets/29c6bc9a-6bbc-488c-af6d-11f7975b8397)
