# core/processor.py

from utils.router import detect_modality
from models.vision import caption_image
from models.audio_transcription import audio_transcription
from models.pdf import extract_pdf_text
from core.memory import memory

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
        raise ValueError(f"❌ Unknown modality for file: {file_path}")

def process_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    memory.add_memory(content, modality="text")
    recalls = memory.query(content, modality_filter="text")
    return format_result(content, recalls)

def process_image(path):
    content = caption_image(path)
    memory.add_memory(content, modality="image")
    recalls = memory.query("describe image", modality_filter="image")
    return format_result(content, recalls)

def process_audio(path):
    content = audio_transcription(path)
    memory.add_memory(content, modality="audio")
    recalls = memory.query("speech", modality_filter="audio")
    return format_result(content, recalls)

def process_pdf(path):
    content = extract_pdf_text(path)
    memory.add_memory(content, modality="pdf")
    recalls = memory.query("pdf content", modality_filter="pdf")
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
