from llm.llm import summarize_document
from llm.prompts import SUMMARY_PROMPT


def analyze_document(document_text):

    result = summarize_document(
        document_text,
        SUMMARY_PROMPT
    )

    return result