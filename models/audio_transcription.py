# core/audio_transcription.py

import whisper

model = whisper.load_model("base")

def audio_transcription(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"]
