from llm.llm import llm

# Store conversation history
chat_history = []


def ask_question(vector_store, question):
    """
    Ask a question using the vector store and conversation history.
    """

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10
        }
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    history = "\n".join(
        [
            f"User: {item['question']}\nAssistant: {item['answer']}"
            for item in chat_history[-5:]
        ]
    )

    prompt = f"""
You are an expert Legal AI Assistant.

Answer ONLY using the document context.

Previous Conversation:
{history}

Document Context:
{context}

Question:
{question}

Rules:
1. Never invent information.
2. If the answer is not in the document, reply:
"I could not find this information in the uploaded document."
3. Keep answers concise and professional.

Answer:
"""

    response = llm.invoke(prompt)

    answer = response.content.strip()

    chat_history.append(
        {
            "question": question,
            "answer": answer
        }
    )

    return {
        "answer": answer,
        "sources": docs
    }