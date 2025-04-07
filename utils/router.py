# utils/router.py

import mimetypes
import os
import sys

# 🔧 Ensure project root is in path (for local imports)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def detect_modality(file_path: str) -> str:
    """
    Detects the type of input file based on its MIME type or extension.
    Returns one of: 'text', 'image', 'audio', 'pdf', or 'unknown'
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    ext = os.path.splitext(file_path)[-1].lower()

    if mime_type:
        if mime_type.startswith("text"):
            return "text"
        elif mime_type.startswith("image"):
            return "image"
        elif mime_type.startswith("audio"):
            return "audio"
        elif mime_type == "application/pdf":
            return "pdf"

    # Fallback to extension
    if ext in [".txt", ".md"]:
        return "text"
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
        return "image"
    elif ext in [".mp3", ".wav", ".ogg", ".m4a"]:
        return "audio"
    elif ext == ".pdf":
        return "pdf"

    return "unknown"
