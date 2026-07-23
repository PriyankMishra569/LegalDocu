import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from services.analyzer import analyze_document
from rag.splitter import split_document
from rag.vector_store import create_vector_store
from rag.qa import ask_question

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Legal Document Analyzer",
    page_icon="⚖️",
    layout="wide"
)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "document_loaded" not in st.session_state:
    st.session_state.document_loaded = False

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("⚖️ Legal AI")

    st.markdown("---")

    st.metric("LLM", "Groq Llama 3.3")
    st.metric("Framework", "LangChain")
    st.metric("Vector DB", "FAISS")

    st.markdown("---")

    st.info(
        "Upload a legal PDF to analyze it and ask questions."
    )

# ---------------------------------------------------
# Main Title
# ---------------------------------------------------

st.title("⚖️ Legal Document Analyzer")

st.write(
    "Upload a legal document and let AI summarize, analyze and answer questions."
)

uploaded_file = st.file_uploader(
    "📂 Upload PDF",
    type=["pdf"]
)

# ---------------------------------------------------
# Build Analysis Once
# ---------------------------------------------------

if uploaded_file and not st.session_state.document_loaded:

    st.success("✅ File Uploaded Successfully")

    st.subheader("📄 Document Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**File Name**")
        st.success(uploaded_file.name)

    with col2:
        st.write("**File Size**")
        st.success(f"{uploaded_file.size/1024:.2f} KB")

    # -----------------------------------------
    # Extract Text
    # -----------------------------------------

    try:

        text = extract_text_from_pdf(uploaded_file)

    except Exception as e:

        st.error(e)
        st.stop()

    # Save text

    st.session_state.document_text = text

    # -----------------------------------------
    # Preview
    # -----------------------------------------

    with st.expander("📄 View Extracted Text"):

        st.text(text[:5000])

    # -----------------------------------------
    # Create Vector Store
    # -----------------------------------------

    try:

        with st.spinner("Creating vector database..."):

            chunks = split_document(text)

            vector_store = create_vector_store(chunks)

            st.session_state.vector_store = vector_store

    except Exception as e:

        st.error(e)
        st.stop()

    # -----------------------------------------
    # Analyze Document
    # -----------------------------------------

    try:

        with st.spinner("Analyzing document..."):

            result = analyze_document(text)

            st.session_state.analysis = result

    except Exception as e:

        st.error(e)
        st.stop()

    st.session_state.document_loaded = True

# ---------------------------------------------------
# Display Analysis
# ---------------------------------------------------

if st.session_state.document_loaded:

    result = st.session_state.analysis

    if result.get("is_legal"):

        st.success("✅ Legal Document Detected")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Document Type", result.get("document_type", "N/A"))

        with col2:
            st.metric("Purpose", result.get("purpose", "N/A"))

        st.markdown("---")

        st.subheader("📝 Summary")
        st.write(result.get("summary", ""))

        st.markdown("---")

        st.subheader("👥 Parties")

        for party in result.get("parties", []):
            st.write("✅", party)

        st.markdown("---")

        st.subheader("📜 Important Clauses")

        for clause in result.get("important_clauses", []):
            st.write("•", clause)

        st.markdown("---")

        st.subheader("📌 Obligations")

        for obligation in result.get("obligations", []):
            st.write("•", obligation)

        st.markdown("---")

        st.subheader("📅 Deadlines")

        deadlines = result.get("deadlines", [])

        if deadlines:
            for deadline in deadlines:
                st.write("•", deadline)
        else:
            st.info("No deadlines found.")

        st.markdown("---")

        st.subheader("⚠️ Risks")

        risks = result.get("risks", [])

        if risks:
            for risk in risks:
                st.error(risk)
        else:
            st.success("No major risks detected.")

    else:

        st.error("❌ Not a legal document.")

        st.write(result.get("reason", ""))

    # ---------------------------------------------------
    # Chat Section
    # ---------------------------------------------------

    st.markdown("---")

    st.header("💬 Chat with your Legal Document")

    # Show previous messages

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    question = st.chat_input(
        "Ask anything about the uploaded document..."
    )

    if question:

        # User Message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        # AI Response

        try:

            with st.spinner("Searching document..."):

                qa_result = ask_question(
                    st.session_state.vector_store,
                    question
                )

            answer = qa_result["answer"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):

                st.markdown(answer)

                with st.expander("📚 Source Chunks"):

                    for i, doc in enumerate(
                        qa_result["sources"],
                        start=1
                    ):

                        st.markdown(f"### Source {i}")

                        st.write(doc.page_content)

                        st.divider()

        except Exception as e:

            st.error(e)