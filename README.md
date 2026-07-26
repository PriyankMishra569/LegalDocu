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