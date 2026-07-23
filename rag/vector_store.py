import os
import hashlib

from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embedding_model


INDEX_DIR = "faiss_indexes"


def _document_hash(chunks):
    """
    Generate a unique hash for the uploaded document.
    """
    document_text = "".join(chunks)
    return hashlib.md5(document_text.encode("utf-8")).hexdigest()


def create_vector_store(chunks):
    """
    Create a FAISS vector store for the document.
    If an index already exists for the same document,
    load it instead of recreating it.
    """

    embeddings = get_embedding_model()

    os.makedirs(INDEX_DIR, exist_ok=True)

    doc_hash = _document_hash(chunks)

    index_path = os.path.join(INDEX_DIR, doc_hash)

    # Load existing index
    if os.path.exists(index_path):

        vector_store = FAISS.load_local(
            index_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

        return vector_store

    # Create new index
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    vector_store.save_local(index_path)

    return vector_store