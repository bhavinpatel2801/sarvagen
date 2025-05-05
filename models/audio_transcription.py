# === Import the Whisper speech-to-text model from OpenAI ===
import whisper

# Load the Whisper model — "base" is a smaller, faster model suited for CPU inference
model = whisper.load_model("base")

# Define a function to perform audio transcription using Whisper
def audio_transcription(audio_path: str) -> str:
    # Transcribe the given audio file and return the result as a dictionary
    result = model.transcribe(audio_path)
    # Extract and return only the transcribed text from the result
    return result["text"]
