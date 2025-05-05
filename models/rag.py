# import necessary libraries
from models.pdf import extract_pdf_text         # Import PDF text extraction function
from core.memory import memory                  # Import memory store instance for vector-based search
import os                                       # Import memory store instance for vector-based search

# Set to track which PDFs have already been ingested to avoid duplicate embeddings
INGESTED_PDFS = set()

# === Function to ingest a PDF into memory (for RAG-style retrieval) ===
def ingest_pdf_to_memory(pdf_path: str):
    # Skip ingestion if this PDF has already been processed
    if pdf_path in INGESTED_PDFS:
        return  # Skip if already added
    content = extract_pdf_text(pdf_path)        # Extract text from the PDF (first 5 pages, max 2000 characters)
    chunks = content.split("\n\n")              # Split text into chunks using paragraph breaks as boundaries, Simple, fast chunking strategy

    # For each non-empty chunk, add to memory
    for chunk in chunks:
        if chunk.strip():                       # Ignore empty chunks
            memory.add_memory(chunk.strip(), source=pdf_path, modality="pdf")   # Track source and modality
    INGESTED_PDFS.add(pdf_path)                 # Mark this PDF as ingested

# === Function to perform a retrieval-augmented generation (RAG)-style query ===
def rag_query(query: str, context_pdf: str = None) -> str:
    # If a context PDF is provided and exists, ingest its content into memory
    if context_pdf and os.path.exists(context_pdf):
        ingest_pdf_to_memory(context_pdf)

    related_chunks = memory.query(query, top_k=5)  # Search memory for top 5 most relevant chunks for the given query
    result = "\n".join([f"- {chunk['content'][:300]}" for chunk in related_chunks])  # Format the output by showing the first 300 characters of each chunk
    return f"🔍 Retrieved from memory:\n{result}"  # Return final result string
