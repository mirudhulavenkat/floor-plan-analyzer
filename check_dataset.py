
import os
import cv2

# Dataset paths
X_PATH = "dataset/X"
Y_PATH = "dataset/Y"

# Get image filenames
x_files = sorted(os.listdir(X_PATH))

y_files = sorted(os.listdir(Y_PATH))

print("===== FLOOR PLAN DATASET =====")

print("Total X images:", len(x_files))
print("Total Y masks:", len(y_files))

# Select first original image
image_name = "1.png"
mask_name = "1 (2).png"

image_path = os.path.join(X_PATH, image_name)
mask_path = os.path.join(Y_PATH, mask_name)

# Read images
image = cv2.imread(image_path)
mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)

# Display information
if image is not None and mask is not None:

    print("\n===== IMAGE INFORMATION =====")
    print("Image name:", image_name)
    print("Image size:", image.shape)

    print("\n===== MASK INFORMATION =====")
    print("Mask name:", mask_name)
    print("Mask size:", mask.shape)

    print("\nDataset loaded successfully!")

else:
    print("\nError: Image or mask not found.")
    print("Check the filenames and folder paths.")
