# import necessary libraries
from utils.router import detect_modality                              # Import function to detect the type of input file (text, image, audio, pdf, etc.)
from models.vision import caption_image                               # Import image captioning function for visual content processing 
from models.audio_transcription import audio_transcription            # Import transcription function to process audio input
from models.pdf import extract_pdf_text                               # Import PDF text extractor function
from core.memory import memory                                        # Import shared memory store for storing and retrieving memories

# === Main router that decides how to process input based on its modality ===
def route_input(file_path: str):
    modality = detect_modality(file_path)                              # Identify the type of input (modality)

    # Route to appropriate processing function based on modality
    if modality == "text":
        return process_text(file_path)
    elif modality == "image":
        return process_image(file_path)
    elif modality == "audio":
        return process_audio(file_path)
    elif modality == "pdf":
        return process_pdf(file_path)
    else:
        raise ValueError(f"❌ Unknown modality for file: {file_path}")  # If modality is not recognized, raise an error

# === Processing function for plain text files ===
def process_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()                                      # Read and clean the file content
    memory.add_memory(content, modality="text")                         # Store the content in memory as text
    recalls = memory.query(content, modality_filter="text")             # Retrieve related text memories
    return format_result(content, recalls)                              # Return formatted output

# === Processing function for image files ===
def process_image(path):
    content = caption_image(path)                                       # Use vision model to generate a caption for the image
    memory.add_memory(content, modality="image")                        # Store the caption in memory as an image modality
    recalls = memory.query("describe image", modality_filter="image")   # Retrieve similar image-based memories
    return format_result(content, recalls)                              # Return formatted output

# === Processing function for audio files ===
def process_audio(path):
    content = audio_transcription(path)                                 # Convert speech to text using transcription model
    memory.add_memory(content, modality="audio")                        # Store transcribed content as audio modality
    recalls = memory.query("speech", modality_filter="audio")           # Retrieve related audio-based memories
    return format_result(content, recalls)                              # Return formatted output

# === Processing function for PDF files ===
def process_pdf(path):
    content = extract_pdf_text(path)                                    # Extract all readable text from PDF
    memory.add_memory(content, modality="pdf")                          # Store extracted content as PDF modality
    recalls = memory.query("pdf content", modality_filter="pdf")        # Retrieve related PDF-based memories
    return format_result(content, recalls)                              # Return formatted output

# === Formats the content and any retrieved memories into a readable output ===
def format_result(content, recalls):
    out = f"🧠 **Input Stored:**\n\n{content}\n\n"                      # Start with the content that was stored
    if recalls:
        out += "📚 **Related Memory Recalls:**\n"                       # Header for memory matches
        for mem in recalls:
            # Show modality and first 100 characters of recalled content
            out += f"- {mem['modality'].capitalize()} → {mem['content'][:100]}...\n"
    else:
        # No similar memory was found
        out += "🕳️ No related past memory found."
    return out                                                          # Return the final formatted output
