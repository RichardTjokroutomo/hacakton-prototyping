import cv2
import numpy as np
import matplotlib.pyplot as plt

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
if box_corners is not None:
    print("corners: ")
    for corner in box_corners:
        cv2.circle(image, tuple(corner[0]), 10, (0, 255, 0), -1)
        print(corner)

    # Display the image with corners
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    # Print the coordinates of the corners
    box_corners_list = [tuple(corner[0]) for corner in box_corners]
    print("Corners of the box:", box_corners_list)
else:
    print("Box not detected.")
