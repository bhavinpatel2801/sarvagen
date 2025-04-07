from models.image_segmentation import image_segmentation

print("== Image Segmentation Tool Test ==")
output_path = image_segmentation("data/test/sample.jpg")
print("Segmented image saved to:", output_path)
