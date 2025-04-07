# models/pdf.py

import fitz  # PyMuPDF

def extract_pdf_text(path: str, max_pages=5) -> str:
    doc = fitz.open(path)
    text = ""
    for page in doc[:max_pages]:
        text += page.get_text()
    return text.strip()[:2000]  # Limit size for now
