from ultralytics import YOLO
from PIL import Image
import cv2

# Load a YOLO model; for specific needs, you might need to fine-tune it
model = YOLO('yolov5s')  # Use a fine-tuned model for best results

# Capture or load the image
img = 'your_image.jpg'
results = model(img)

# Extract bounding boxes around detected objects
boxes = results.xyxy[0]  # Array of bounding boxes detected in the image


for box in boxes:
    xmin, ymin, xmax, ymax = map(int, box[:4])  # Get coordinates
    cropped_box = Image.open(img).crop((xmin, ymin, xmax, ymax))
