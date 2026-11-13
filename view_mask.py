
import cv2
import numpy as np

mask = cv2.imread("dataset/Y/1 (2).png")

# Resize for easy viewing
preview = cv2.resize(mask, (700, 700))

cv2.imwrite("output/mask_preview.png", preview)

print("Mask preview saved successfully!")
