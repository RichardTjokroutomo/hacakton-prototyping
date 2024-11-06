from ultralytics import YOLO
from PIL import Image
import cv2
import pytesseract

# Load a YOLO model; for specific needs, you might need to fine-tune it
model = YOLO('yolov8s.pt')  # Use a fine-tuned model for best results
print("================================ FINISHED LOADING MODEL ===================================")

# Capture or load the image
img = './test-img.jpg'
results = model(img)


# Extract bounding boxes around detected objects
boxes = results.xyxy[0]  # Array of bounding boxes detected in the image
print("================================ BOUNDING BOX EXTRACTED ===================================")

for box in boxes:
    xmin, ymin, xmax, ymax = map(int, box[:4])  # Get coordinates
    cropped_box = Image.open(img).crop((xmin, ymin, xmax, ymax))
print("================================ COORDINATES ASSIGNED ===================================")


# OCR
text = pytesseract.image_to_string(cropped_box)
print("Extracted text:", text)