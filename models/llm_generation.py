# core/tools_llm_generation.py

import subprocess

def llm_generation(prompt: str) -> str:
    try:
        result = subprocess.run(["ollama", "run", "mixtral", prompt], capture_output=True, text=True,  encoding="utf-8")
        return result.stdout
    except Exception as e:
        return f"❌ Failed to run Mixtral via Ollama: {str(e)}"
