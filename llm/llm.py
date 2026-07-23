import os
import json

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from models.legal_document import LegalDocument

load_dotenv()

# -------------------------------------------------------
# Initialize Groq LLM
# -------------------------------------------------------

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.2,
)

# -------------------------------------------------------
# Helper Function
# -------------------------------------------------------

def clean_json(content: str) -> str:
    """
    Remove markdown code fences from the LLM response.
    """

    content = content.strip()

    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.startswith("```"):
        content = content.replace("```", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    return content.strip()


# -------------------------------------------------------
# Summarize Document
# -------------------------------------------------------

def summarize_document(document_text: str, prompt: str):

    response = llm.invoke(
        f"{prompt}\n\n{document_text}"
    )

    content = clean_json(response.content)

    try:

        data = json.loads(content)

        # Validate using Pydantic
        validated = LegalDocument(**data)

        return validated.model_dump()

    except json.JSONDecodeError as e:

        raise ValueError(
            f"Invalid JSON returned by LLM.\n\n{content}"
        ) from e

    except Exception as e:

        raise ValueError(
            f"Validation Error:\n{e}"
        ) from e