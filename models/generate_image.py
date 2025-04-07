# models/generate_image.py

from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import uuid

# Load on first call only
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cpu")  # CPU mode

def generate_image(prompt: str, output_dir="data/generated/") -> str:
    image = pipe(prompt).images[0]
    out_path = f"{output_dir}gen_{uuid.uuid4().hex[:6]}.png"
    image.save(out_path)
    return out_path
