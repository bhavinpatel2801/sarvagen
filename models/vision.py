# models/vision.py

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load model once
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(path: str) -> str:
    image = Image.open(path).convert("RGB")
    inputs = processor(image, return_tensors="pt").to(model.device)
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)
