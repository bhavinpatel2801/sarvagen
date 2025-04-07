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
from utils.router import detect_modality

print("== Modality Detection ==")
print(detect_modality("data/test/sample.txt"))
print(detect_modality("data/test/sample.pdf"))
print(detect_modality("data/test/sample.jpg"))
print(detect_modality("data/test/sample.wav"))