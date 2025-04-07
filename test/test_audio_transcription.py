from models.audio_transcription import audio_transcription

print("== Audio Transcription Test ==")
transcription = audio_transcription("data/test/sample.mp3")
print("Transcription:", transcription)
