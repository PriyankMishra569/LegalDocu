import fitz

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.

    Parameters:
        uploaded_file: Streamlit uploaded file object

    Returns:
        str: Extracted text from all pages
    """

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text