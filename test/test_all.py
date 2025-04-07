import sys
import os
# 🔧 Add the project root directory to Python's import path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# Add current folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Add parent folder (for core/, models/, utils/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from core.processor import route_input
from core.memory import MemoryStore
from core.agent import agent_controller
from core.tools import search_memory_tool
from models.vision import caption_image
from models.pdf import extract_pdf_text
from models.generate_image import generate_image
from models.generate_audio import synthesize_speech

sample_text = "data/test/sample.txt"
sample_pdf = "data/test/sample.pdf"
sample_image = "data/test/sample.jpg"
sample_audio = "data/test/sample.wav"

results = []

try:
    results.append(("route_input (PDF)", route_input(sample_pdf)))
except Exception as e:
    results.append(("route_input (PDF)", f"❌ Error: {str(e)}"))

try:
    mem = MemoryStore()
    mem.add_memory("Van Gogh was a painter.", source="test", modality="text")
    res = mem.query("Who is Van Gogh?")
    results.append(("MemoryStore", res))
except Exception as e:
    results.append(("MemoryStore", f"❌ Error: {str(e)}"))

try:
    result = agent_controller("Who painted Starry Night?")
    results.append(("agent_controller", result))
except Exception as e:
    results.append(("agent_controller", f"❌ Error: {str(e)}"))

try:
    result = search_memory_tool("Van Gogh")
    results.append(("search_memory_tool", result))
except Exception as e:
    results.append(("search_memory_tool", f"❌ Error: {str(e)}"))

try:
    result = caption_image(sample_image)
    results.append(("caption_image", result))
except Exception as e:
    results.append(("caption_image", f"❌ Error: {str(e)}"))

try:
    result = extract_pdf_text(sample_pdf)
    results.append(("extract_pdf_text", result))
except Exception as e:
    results.append(("extract_pdf_text", f"❌ Error: {str(e)}"))

try:
    result = generate_image("A samurai warrior on Mars")
    results.append(("generate_image", result))
except Exception as e:
    results.append(("generate_image", f"❌ Error: {str(e)}"))

try:
    result = synthesize_speech("This is SarvaGen speaking.")
    results.append(("synthesize_speech", result))
except Exception as e:
    results.append(("synthesize_speech", f"❌ Error: {str(e)}"))

for name, output in results:
    print(f"\n==== {name} ====")
    print(output)
