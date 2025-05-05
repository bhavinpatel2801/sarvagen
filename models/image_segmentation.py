from PIL import Image                               # Import PIL for image loading and saving
import torch                                        # Import PyTorch for model handling
import numpy as np                                  # NumPy is used for array manipulation
import torchvision.transforms as T                  # Torchvision transforms (not used here but commonly needed for image pipelines)
from segment_anything import sam_model_registry, SamPredictor      # Import SAM (Segment Anything Model) utilities
import os                                           # OS for creating directories and handling file paths

# Set path to your downloaded SAM checkpoint
sam_checkpoint = "checkpoints/sam_vit_b.pth"  # Make sure this file exists!

# Load the SAM model using the "vit_b" variant
sam = sam_model_registry["vit_b"](checkpoint=sam_checkpoint)
# Move the model to CPU since you’re running without GPU
sam.to("cpu")
# Create a predictor object for performing segmentation
predictor = SamPredictor(sam)

# === Function to segment the image based on a center point ===
def image_segmentation(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")   # Load the image and convert to RGB (removes alpha channel if present)
    image_np = np.array(image)                      # Convert image to NumPy array for SAM model compatibility
    predictor.set_image(image_np)                   # Set the image in the SAM predictor

    # Define a single input point at the center of the image
    input_point = np.array([[image_np.shape[1]//2, image_np.shape[0]//2]])
    input_label = np.array([1])                     # Label the point as foreground (1 = object to segment)

    # Predict the segmentation mask using the given point
    masks, _, _ = predictor.predict(
        point_coords=input_point,                   # Coordinates of guidance point
        point_labels=input_label,                   # Label of point: 1 = foreground
        multimask_output=False                      # Return only one best mask
    )

    # ✅ Save mask output image
    os.makedirs("data/generated", exist_ok=True)    # Create output directory if it doesn’t exist
    output_path = "data/generated/mask_output.png"  # Define output path for the segmented mask
    mask_image = Image.fromarray((masks[0] * 255).astype(np.uint8))   # Convert mask to image format: boolean mask → 0/255 grayscale → uint8 image
    mask_image.save(output_path)                    # Save the segmented mask as a PNG image

    return output_path                              # Return the saved mask image path
