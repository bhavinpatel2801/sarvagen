# core/tools.py

from models.vision import caption_image
from models.pdf import extract_pdf_text
from models.generate_image import generate_image
from models.generate_audio import synthesize_speech
from core.memory import memory
from models.image_segmentation import image_segmentation
from models.audio_transcription import audio_transcription
from models.rag import rag_query
from models.llm_generation import llm_generation

# Tool 1: Memory Retriever
def search_memory_tool(query: str) -> str:
    recalls = memory.query(query)
    return "\n".join([f"- {r['modality']} → {r['content'][:150]}..." for r in recalls]) or "🕳️ No related memory found."

# Tool 2: Identity (Echo)
def identity_tool(query: str) -> str:
    return f"🗣️ Echoing input: {query}"

# Tool 3: Image Captioning
def image_caption_tool(path: str) -> str:
    return caption_image(path)

# Tool 4: PDF Summary
def pdf_summary_tool(path: str) -> str:
    return extract_pdf_text(path)

# Tool 5: Image Generation
def image_generate_tool(prompt: str) -> str:
    return generate_image(prompt)

# Tool 6: Audio Generation
def audio_generate_tool(text: str) -> str:
    return synthesize_speech(text)

# Tool 7: Image Segmentation
def image_segmentation_tool(image_path: str) -> str:
    return image_segmentation(image_path)

# Tool 8: Audio Transcription
def audio_transcription_tool(audio_path: str) -> str:
    return audio_transcription(audio_path)

# Tool 9: RAG-based Memory QA
def rag_tool(query: str) -> str:
    return rag_query(query)

# Tool 10: LLM Generation via Ollama
def llm_generation_tool(prompt: str) -> str:
    return llm_generation(prompt)


# ✅ Unified Tool Registry
TOOL_REGISTRY = {
    "memory": search_memory_tool,
    "echo": identity_tool,
    "caption_image": image_caption_tool,
    "summarize_pdf": pdf_summary_tool,
    "generate_image": image_generate_tool,
    "generate_audio": audio_generate_tool,
    "image_segmentation": image_segmentation_tool,
    "audio_transcription": audio_transcription_tool,
    "rag": rag_tool,
    "llm_generation": llm_generation_tool
}

def list_tools():
    return list(TOOL_REGISTRY.keys())

def use_tool(name: str, input_text: str):
    tool = TOOL_REGISTRY.get(name)
    if not tool:
        return f"❌ Tool '{name}' not found."
    return tool(input_text)
