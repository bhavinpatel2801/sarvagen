# import necessary libraries
import mimetypes                                  # Import the mimetypes module to guess file types based on extension
import os                                         # Import os for file path manipulation
import sys                                        # Import sys to modify the Python path

# Ensure project root is in path (for local imports)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# === Function to detect the modality/type of a given file ===
def detect_modality(file_path: str) -> str:
    """
    Detects the type of input file based on its MIME type or extension.
    Returns one of: 'text', 'image', 'audio', 'pdf', or 'unknown'
    """
    mime_type, _ = mimetypes.guess_type(file_path) # Guess the MIME type based on file extension                                             
    ext = os.path.splitext(file_path)[-1].lower()  # Extract file extension and convert to lowercase

    # === MIME-based detection (primary logic) ===
    if mime_type:
        if mime_type.startswith("text"):
            return "text"
        elif mime_type.startswith("image"):
            return "image"
        elif mime_type.startswith("audio"):
            return "audio"
        elif mime_type == "application/pdf":
            return "pdf"

    # === Fallback to extension-based detection (backup logic) ===
    if ext in [".txt", ".md"]:
        return "text"
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
        return "image"
    elif ext in [".mp3", ".wav", ".ogg", ".m4a"]:
        return "audio"
    elif ext == ".pdf":
        return "pdf"

    return "unknown"                                # Return "unknown" if nothing matches
