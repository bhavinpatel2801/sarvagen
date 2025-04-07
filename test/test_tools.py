from core.tools import search_memory_tool, use_tool

print("== Tool: Memory Search ==")
print(search_memory_tool("Van Gogh"))

print("\n== Tool: Image Captioning ==")
print(use_tool("caption_image", "data/test/sample.jpg"))

print("\n== Tool: PDF Summary ==")
print(use_tool("summarize_pdf", "data/test/sample.pdf"))