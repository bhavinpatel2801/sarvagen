# import necessary libraries
from transformers import BlipProcessor, BlipForConditionalGeneration     # Import BLIP (Bootstrapped Language Image Pretraining) processor and model from Hugging Face
from PIL import Image                                                    # PIL is used to open and convert image files
import torch                                                             # PyTorch is used for tensor manipulation and model inference

# === Load BLIP model and processor once globally ===
# Load the BLIP image captioning processor (handles image preprocessing and tokenization)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# Load the BLIP model for generating captions from images
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# === Main function to caption an image ===
def caption_image(path: str) -> str:
    image = Image.open(path).convert("RGB")                               # Open the image and convert to RGB (ensures consistency for models)
    inputs = processor(image, return_tensors="pt").to(model.device)       # Preprocess the image into input tensors (and send them to model's device: CPU or GPU)
    out = model.generate(**inputs)                                        # Generate caption using the BLIP model
    return processor.decode(out[0], skip_special_tokens=True)             # Decode the generated token IDs into a human-readable string