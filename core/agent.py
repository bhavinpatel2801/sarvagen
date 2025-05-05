# import necessary libraries
from core.tools import use_tool                                            # Import the tool usage interface from the internal core module
from utils.prompt import FEW_SHOT_TOOL_REASONING                           # Import a predefined prompt used for few-shot reasoning (a string with examples)
import os                                                                  # Import standard OS library for file operations

# Define a function `agent_controller` that routes a given input (file or query) to the correct AI tool
def agent_controller(input_path: str, reasoning_text: str = "") -> str:    
    input_text = ""                                                        # Initialize input_text as empty string

    # If the input is a text file, read its content
    if input_path.endswith(".txt"):
        with open(input_path, "r", encoding="utf-8") as f:
            input_text = f.read().strip()                                  # Read file and remove leading/trailing whitespace
    else:
        input_text = os.path.basename(input_path).lower()                  # If not a .txt, use the file name as the input text

    # If a reasoning string is passed, use it; otherwise fallback to the extracted input text
    reasoning_base = reasoning_text.lower() if reasoning_text else input_text.lower()

    # Begin building a trace string that logs the reasoning steps
    trace = "🔍 Agent is reasoning with few-shot examples...\n\n"
    trace += FEW_SHOT_TOOL_REASONING + "\n"

    # === Tool Routing Logic ===
    # Decide which tool to use based on the reasoning text content
    if "summarize" in reasoning_base and "pdf" in input_path.lower():
        steps = [("summarize_pdf", input_path)]                            # Route to PDF summarization                       
    elif "caption" in reasoning_base or "describe" in reasoning_base or "what" in reasoning_base:
        steps = [("caption_image", input_path)]                            # Route to image captioning
    elif "generate" in reasoning_base and "image" in reasoning_base:
        steps = [("generate_image", reasoning_base)]                       # Route to image generation from text
    elif "segment" in reasoning_base or "mask" in reasoning_base:
        steps = [("image_segmentation", input_path)]                       # Route to image segmentation
    elif "transcribe" in reasoning_base or "audio" in reasoning_base:
        steps = [("audio_transcription", input_path)]                      # Route to audio transcription
    elif "rag" in reasoning_base or "retrieve" in reasoning_base:
        steps = [("rag_query", reasoning_base)]                            # Route to retrieval-augmented generation query
    elif "llm" in reasoning_base or "text" in reasoning_base or "complete" in reasoning_base:
        steps = [("llm_generation", reasoning_base)]                       # Route to LLM-based text generation
    elif "who" in reasoning_base or "what" in reasoning_base:
        steps = [("memory", reasoning_base)]                               # Route to memory lookup (likely querying past interactions)
    else:
        steps = [("echo", reasoning_base)]                                 # Fallback tool that just echoes the input

    # === Tool Execution Loop ===
    for i, (tool, payload) in enumerate(steps):
        trace += f"\nStep {i+1}:\n"                                        # Log the step number
        trace += f"🧠 Thought: Use `{tool}` for this input\n"              # Log the internal decision
        trace += f"🔧 Action: Calling `{tool}`...\n"                       # Log the action
        result = use_tool(tool, payload)                                    # Call the appropriate tool with payload
        trace += f"📤 Result: {result[:500]}...\n"                         # Append first 500 chars of result to trace

    return trace                                                           # Return the full trace of actions and outcomes
