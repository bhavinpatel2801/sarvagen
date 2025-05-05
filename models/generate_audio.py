import pyttsx3                                # Import pyttsx3 for text-to-speech synthesis (offline, works on CPU)                                     
import uuid                                   # Import uuid for generating unique filenames
import os                                     # Import os for file and directory operations

# Define a function to synthesize speech from text and save it as an audio file
def synthesize_speech(text: str, output_dir="data/generated/") -> str:
    # Create the output directory if it doesn't already exist
    os.makedirs(output_dir, exist_ok=True)
    # Initialize the pyttsx3 speech engine (uses system TTS voices)
    engine = pyttsx3.init()
    # Generate a unique filename using UUID (first 6 chars) for saving the audio
    out_path = os.path.join(output_dir, f"speech_{uuid.uuid4().hex[:6]}.mp3")
    # Queue the text-to-speech conversion and save the result to file
    engine.save_to_file(text, out_path)
    # Block until the speech synthesis and file write is completed
    engine.runAndWait()
    # Return the path to the generated speech file
    return out_path
