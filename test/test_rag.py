from models.rag import rag_query

print("== RAG PDF Tool Test ==")
result = rag_query("What did Van Gogh do?", context_pdf="data/test/sample.pdf")
print(result)
