import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract

# Load the image
image_path = './test-img.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection to find contours
edges = cv2.Canny(image_gray, 50, 150, apertureSize=3)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables for storing corners
box_corners = None

# Filter contours to find the rectangular box
for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Look for a rectangle (4 vertices)
    if len(approx) == 4:
        box_corners = approx
        break

# Draw the corners on the image for visualization
res = []
if box_corners is not None:
    print("corners: ")
    for corner in box_corners:
        cv2.circle(image, tuple(corner[0]), 10, (0, 255, 0), -1)
        res.append(corner)
        print(corner)
else:
    print("Box not detected.")

top_left_corner = (res[0][0][0], res[0][0][1])
bottom_right_corner = (res[2][0][0], res[2][0][1])
print(top_left_corner)
print(bottom_right_corner)

# Open the image
image = Image.open('./test-img.jpg')

# Crop using the bounding box coordinates
cropped_image = image.crop((top_left_corner[0], top_left_corner[1], bottom_right_corner[0], bottom_right_corner[1]))
cropped_image.save('cropped_image.jpg')  # Save the cropped image


import easyocr

reader = easyocr.Reader(['en'])  # Specify language(s)
text = reader.readtext('./cropped_image.jpg', detail=0)  # detail=0 returns text only
print("Extracted Text:", text)
