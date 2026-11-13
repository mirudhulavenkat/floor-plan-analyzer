
import cv2
import numpy as np

mask = cv2.imread("dataset/Y/1 (2).png")

if mask is None:
    print("Mask not found!")
    exit()

pixels = mask.reshape(-1, 3)

colors, counts = np.unique(
    pixels,
    axis=0,
    return_counts=True
)

# Sort by highest pixel count
indices = np.argsort(counts)[::-1]

print("===== MASK ANALYSIS =====")
print("Total unique colours:", len(colors))

print("\n===== TOP 20 COLOURS =====")

for i in indices[:20]:
    percentage = counts[i] / len(pixels) * 100

    print(
        "BGR:", colors[i].tolist(),
        "| Pixels:", counts[i],
        "| Percentage:", round(percentage, 2), "%"
    )
