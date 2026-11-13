
import cv2
import os

# Dataset paths
x_folder = "dataset/X"
y_folder = "dataset/Y"

# Create output folder
os.makedirs("output", exist_ok=True)

# Get image filenames
x_files = os.listdir(x_folder)
y_files = os.listdir(y_folder)

# Match image and mask names
def get_key(filename):
    return filename.replace(" (2).png", ".png")

y_map = {get_key(f): f for f in y_files}

# Select first 3 matching images
count = 0

print("===== OVERLAY GENERATION =====")

for x_file in sorted(
    x_files,
    key=lambda f: int(os.path.splitext(f)[0])
):
    if x_file not in y_map:
        continue

    # Load original image
    image = cv2.imread(os.path.join(x_folder, x_file))

    # Load corresponding mask
    mask = cv2.imread(
        os.path.join(y_folder, y_map[x_file])
    )

    if image is None or mask is None:
        print("Image loading failed:", x_file)
        continue

    # Match image dimensions
    if image.shape[:2] != mask.shape[:2]:
        mask = cv2.resize(
            mask,
            (image.shape[1], image.shape[0])
        )

    # Blend original image and mask
    overlay = cv2.addWeighted(
        image, 0.6,
        mask, 0.4,
        0
    )

    count += 1

    # Save overlay
    output_path = f"output/overlay_{count}.png"
    cv2.imwrite(output_path, overlay)

    print("Created:", output_path)

    if count == 3:
        break

print("\nTotal overlays created:", count)
print("Overlay generation completed!")
