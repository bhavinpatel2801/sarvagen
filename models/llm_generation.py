# Import the subprocess module to execute terminal commands from Python
import subprocess

# Define a function that generates text from a prompt using the Mixtral model via Ollama
def llm_generation(prompt: str) -> str:
    try:
        # Run the Ollama command-line tool with the Mixtral model and input prompt
        result = subprocess.run(
            ["ollama", "run", "mixtral", prompt],  # Command and arguments
            capture_output=True,                   # Capture stdout and stderr
            text=True,                             # Return output as string, not bytes
            encoding="utf-8"                       # Set proper encoding
        )

        # Return the generated output (standard output from the subprocess)
        return result.stdout

    except Exception as e:
        # In case of error (e.g., Ollama not installed, model not loaded), return error message
        return f"❌ Failed to run Mixtral via Ollama: {str(e)}"
