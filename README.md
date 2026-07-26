# 📄 Legal Document Analyzer using AI

An AI-powered web application that analyzes legal PDF documents using Large Language Models (LLMs). The application generates concise summaries, extracts key information, and allows users to ask questions about the uploaded document using Retrieval-Augmented Generation (RAG).

## 🎯 Project Overview

Legal Document Analyzer is designed to simplify the understanding of legal documents by leveraging modern AI technologies. Users can upload legal PDF files, receive AI-generated summaries, and ask natural language questions to obtain accurate answers based on the document's content.

This project uses Groq's Llama 3.3 model, LangChain, FAISS vector database, and Streamlit to provide a fast and interactive experience.

## ✨ Key Features

- 📂 Upload legal PDF documents
- 📄 Extract text from PDFs
- 🤖 Generate AI-powered summaries
- ❓ Ask questions about uploaded documents
- 🔍 Semantic search using FAISS Vector Database
- ⚡ Fast inference using Groq Llama 3.3
- 🌐 Interactive Streamlit web interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Streamlit | Web Application Framework |
| LangChain | LLM Orchestration |
| Groq API | Large Language Model |
| FAISS | Vector Database |
| PyMuPDF | PDF Text Extraction |
| Sentence Transformers | Text Embeddings |
| python-dotenv | Environment Variable Management |

---

## 🏗️ System Architecture

```
                Upload PDF
                     │
                     ▼
          PDF Text Extraction
              (PyMuPDF)
                     │
                     ▼
            Text Chunking
                     │
                     ▼
     Sentence Transformer Embeddings
                     │
                     ▼
            FAISS Vector Store
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
 AI Summary Generation     Question Answering
      (Groq LLM)            (RAG + LangChain)
         │                       │
         └───────────┬───────────┘
                     ▼
             Streamlit Interface
```

---

# 📂 Project Structure

```
LegalDoc/
│
├── app.py                      # Streamlit application
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── .env.example                # Environment variables template
│
├── llm/
│   ├── llm.py
│   └── prompts.py
│
├── rag/
│   ├── splitter.py
│   ├── vector_store.py
│   └── qa.py
│
├── services/
│   └── analyzer.py
│
├── utils/
│   └── pdf_reader.py
│
└── sample_documents/
    ├── Service_Agreement.pdf
    ├── Employment_Agreement.pdf
    └── NDA.pdf
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/LegalDoc.git
```

Navigate to the project folder

```bash
cd LegalDoc
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a file named `.env`

Add the following:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

After launching, open:

```
http://localhost:8501
```

---

# 📖 How to Use

1. Launch the application.
2. Upload a legal PDF document.
3. Wait for the AI to process the document.
4. Read the generated summary.
5. Ask questions related to the uploaded document.
6. Receive AI-generated answers based on the document content.
