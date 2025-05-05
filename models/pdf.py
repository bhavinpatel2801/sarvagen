# Import PyMuPDF (fitz), a fast library for reading and extracting content from PDF files
import fitz  # PyMuPDF

# Define a function to extract text from the first few pages of a PDF
def extract_pdf_text(path: str, max_pages=5) -> str:
    doc = fitz.open(path)                   # Open the PDF file at the specified path
    text = ""                               # Initialize an empty string to accumulate extracted text

    # Loop through the first `max_pages` pages of the document
    for page in doc[:max_pages]:
        text += page.get_text()  # Extract and append text from the current page

    # Return the first 2000 characters of stripped text (to avoid overloading downstream models)
    return text.strip()[:2000]
