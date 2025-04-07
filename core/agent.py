from core.tools import use_tool
from utils.prompt import FEW_SHOT_TOOL_REASONING
import os

def agent_controller(input_path: str, reasoning_text: str = "") -> str:
    input_text = ""

    if input_path.endswith(".txt"):
        with open(input_path, "r", encoding="utf-8") as f:
            input_text = f.read().strip()
    else:
        input_text = os.path.basename(input_path).lower()

    # Use user's reasoning text if available
    reasoning_base = reasoning_text.lower() if reasoning_text else input_text.lower()

    trace = "🔍 Agent is reasoning with few-shot examples...\n\n"
    trace += FEW_SHOT_TOOL_REASONING + "\n"

    if "summarize" in reasoning_base and "pdf" in input_path.lower():
        steps = [("summarize_pdf", input_path)]
    elif "caption" in reasoning_base or "describe" in reasoning_base or "what" in reasoning_base:
        steps = [("caption_image", input_path)]
    elif "generate" in reasoning_base and "image" in reasoning_base:
        steps = [("generate_image", reasoning_base)]
    elif "speak" in reasoning_base or "voice" in reasoning_base:
        steps = [("generate_audio", reasoning_base)]
    elif "who" in reasoning_base or "what" in reasoning_base:
        steps = [("memory", reasoning_base)]
    else:
        steps = [("echo", reasoning_base)]

    for i, (tool, payload) in enumerate(steps):
        trace += f"\nStep {i+1}:\n"
        trace += f"🧠 Thought: Use `{tool}` for this input\n"
        trace += f"🔧 Action: Calling `{tool}`...\n"
        result = use_tool(tool, payload)
        trace += f"📤 Result: {result[:500]}...\n"

    return trace
