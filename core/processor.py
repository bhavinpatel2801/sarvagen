# core/processor.py

from utils.router import detect_modality
from core.memory import MemoryStore

memory = MemoryStore()

def route_input(file_path: str):
    modality = detect_modality(file_path)

    if modality == "text":
        return process_text(file_path)
    elif modality == "image":
        return process_image(file_path)
    elif modality == "audio":
        return process_audio(file_path)
    elif modality == "pdf":
        return process_pdf(file_path)
    else:
        raise ValueError(f"Unknown modality for file: {file_path}")


def process_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    memory.add_memory(content, modality="text")
    recalls = memory.query(content)
    return format_result(content, recalls)

def process_image(path):
    # Placeholder: Captioning will be added later
    content = f"Image file path: {path}"
    memory.add_memory(content, modality="image")
    recalls = memory.query("image")
    return format_result(content, recalls)

def process_audio(path):
    # Placeholder: Whisper transcription will be added later
    content = f"Audio file path: {path}"
    memory.add_memory(content, modality="audio")
    recalls = memory.query("audio")
    return format_result(content, recalls)

def process_pdf(path):
    content = f"PDF file path: {path}"
    memory.add_memory(content, modality="pdf")
    recalls = memory.query("pdf")
    return format_result(content, recalls)


def format_result(content, recalls):
    out = f"🧠 **Input Stored:**\n\n{content}\n\n"
    if recalls:
        out += "📚 **Related Memory Recalls:**\n"
        for mem in recalls:
            out += f"- {mem['modality'].capitalize()} → {mem['content'][:100]}...\n"
    else:
        out += "🕳️ No related past memory found."
    return out

