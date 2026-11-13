
import cv2
import numpy as np
import os

# 1. Load segmentation mask
mask_path = "dataset/Y/1 (2).png"
mask = cv2.imread(mask_path)

if mask is None:
    print("Error: Mask not found!")
    exit()

# 2. Detect teal regions
lower = np.array([130, 130, 0])
upper = np.array([155, 155, 20])

room_mask = cv2.inRange(mask, lower, upper)

# 3. Find connected regions
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    room_mask,
    connectivity=8
)

# 4. Create output image
result = mask.copy()
room_count = 0

print("===== ROOM EXTRACTION =====")

for i in range(1, num_labels):

    area = stats[i, cv2.CC_STAT_AREA]

    # Ignore small regions
    if area > 5000:

        room_count += 1

        # Extract individual region
        component = (labels == i).astype(np.uint8)

        # Find actual contour
        contours, _ = cv2.findContours(
            component,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Draw contour boundary
        cv2.drawContours(
            result,
            contours,
            -1,
            (0, 0, 255),
            4
        )

        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]

        print(f"Region {room_count}")
        print("Area:", area, "pixels")
        print("Position:", x, y)
        print("-------------------")

# 5. Save output images
os.makedirs("output", exist_ok=True)

cv2.imwrite("output/room_candidates.png", result)
cv2.imwrite("output/room_mask.png", room_mask)

print("\nTotal candidate regions:", room_count)
print("Room extraction completed!")
print("Images saved in output folder.")
