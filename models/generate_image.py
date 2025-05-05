# Import the Stable Diffusion model pipeline from Hugging Face's diffusers library
from diffusers import StableDiffusionPipeline                    
import torch                                                # Import torch to set device (CPU in this case)
from PIL import Image                                       # Import PIL for image processing
import uuid                                                 # UUID is used to create unique filenames for generated images

# === Model Loading (runs once when the script/module is first used) ===
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cpu")  # CPU mode,  Move the pipeline to CPU for inference (because your setup does not have a GPU)

# === Main Function to Generate Image from Text Prompt ===
def generate_image(prompt: str, output_dir="data/generated/") -> str:
    image = pipe(prompt).images[0]                                   # Generate an image from the prompt; returns a list of images (grab the first one)
    out_path = f"{output_dir}gen_{uuid.uuid4().hex[:6]}.png"         # Create a unique output path using UUID (first 6 chars for brevity)
    image.save(out_path)                                             # Save the generated image to the specified path
    return out_path                                                  # Return the path of the saved image
