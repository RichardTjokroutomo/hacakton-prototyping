from ultralytics import YOLO
model = YOLO('yolov8n.pt')  # Use a pre-trained model or your own

results = model.predict(source='test-img.jpg', conf=0.5)
x1, y1, x2, y2 = 1, 1, 1, 1
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0]  # Top-left and bottom-right corner coordinates


from PIL import Image

# Open the image
image = Image.open('test-img.jpg')
print(x1)
print(y1)
print(x2)
print(y2)

# Crop using the bounding box coordinates
cropped_image = image.crop((x1, y1, x2, y2))
cropped_image.save('cropped_image.jpg')  # Save the cropped image
