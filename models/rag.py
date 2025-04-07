# core/tools_rag.py

from models.pdf import extract_pdf_text
from core.memory import memory
import os

# ✅ Optional: Track ingested PDFs to avoid re-embedding
INGESTED_PDFS = set()

def ingest_pdf_to_memory(pdf_path: str):
    if pdf_path in INGESTED_PDFS:
        return  # Skip if already added
    content = extract_pdf_text(pdf_path)
    chunks = content.split("\n\n")  # Simple paragraph-based chunking
    for chunk in chunks:
        if chunk.strip():
            memory.add_memory(chunk.strip(), source=pdf_path, modality="pdf")
    INGESTED_PDFS.add(pdf_path)

def rag_query(query: str, context_pdf: str = None) -> str:
    if context_pdf and os.path.exists(context_pdf):
        ingest_pdf_to_memory(context_pdf)

    related_chunks = memory.query(query, top_k=5)
    result = "\n".join([f"- {chunk['content'][:300]}" for chunk in related_chunks])
    return f"🔍 Retrieved from memory:\n{result}"
