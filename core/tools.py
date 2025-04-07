# core/tools.py


from models.vision import caption_image
from models.pdf import extract_pdf_text
from models.generate_image import generate_image
from models.generate_audio import synthesize_speech
from core.memory import MemoryStore

memory = MemoryStore()

# Tool 1: Memory Retriever
def search_memory_tool(query: str) -> str:
    recalls = memory.query(query)
    return "\n".join([f"- {r['modality']} → {r['content'][:150]}..." for r in recalls])

# Tool 2: Identity (Echo)
def identity_tool(query: str) -> str:
    return f"Echoing input: {query}"

# Tool 3: Image Captioning
def image_caption_tool(path: str) -> str:
    return caption_image(path)

# Tool 4: PDF Summary
def pdf_summary_tool(path: str) -> str:
    return extract_pdf_text(path)

def image_generate_tool(prompt: str) -> str:
    return generate_image(prompt)

def audio_generate_tool(text: str) -> str:
    return synthesize_speech(text)

# ✅ Tool Registry (all tools listed here)
TOOL_REGISTRY = {
    "memory": search_memory_tool,
    "echo": identity_tool,
    "caption_image": image_caption_tool,
    "summarize_pdf": pdf_summary_tool,
    "generate_image": image_generate_tool,
    "generate_audio": audio_generate_tool,
    "web_search": web_search,
    "image_segmentation": image_segmentation,
    "code_interpreter": code_interpreter,
    "audio_transcription": audio_transcription,
    "rag": rag,
    "llm_generation": llm_generation
}


# List tools for UI/debugging
def list_tools():
    return list(TOOL_REGISTRY.keys())

# Use a specific tool by name
def use_tool(name: str, input_text: str):
    tool = TOOL_REGISTRY.get(name)
    if not tool:
        return f"❌ Tool '{name}' not found."
    return tool(input_text)
