# models/generate_audio.py
import pyttsx3
import uuid
import os

def synthesize_speech(text: str, output_dir="data/generated/") -> str:
    os.makedirs(output_dir, exist_ok=True)
    engine = pyttsx3.init()
    out_path = os.path.join(output_dir, f"speech_{uuid.uuid4().hex[:6]}.mp3")
    engine.save_to_file(text, out_path)
    engine.runAndWait()
    return out_path
