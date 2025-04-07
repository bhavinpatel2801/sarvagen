from PIL import Image
import torch
import numpy as np
import torchvision.transforms as T
from segment_anything import sam_model_registry, SamPredictor
import os

# ✅ Set path to your downloaded SAM checkpoint
sam_checkpoint = "checkpoints/sam_vit_b.pth"  # Make sure this file exists!

# ✅ Load SAM model
sam = sam_model_registry["vit_b"](checkpoint=sam_checkpoint)
sam.to("cpu")
predictor = SamPredictor(sam)

def image_segmentation(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")
    image_np = np.array(image)

    predictor.set_image(image_np)

    # For testing, use center point of the image
    input_point = np.array([[image_np.shape[1]//2, image_np.shape[0]//2]])
    input_label = np.array([1])

    masks, _, _ = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=False
    )

    # ✅ Save mask output image
    os.makedirs("data/generated", exist_ok=True)
    output_path = "data/generated/mask_output.png"
    mask_image = Image.fromarray((masks[0] * 255).astype(np.uint8))
    mask_image.save(output_path)

    return output_path
