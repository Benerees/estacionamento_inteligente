import os
import cv2
from ultralytics import YOLO

image_path = 'C:/Users/dani/Downloads/imagemTeste.jpg'
output_path = 'D:/estacionamento_inteligente/data/result.JPEG'


# Load the model
model = YOLO("D:/estacionamento_inteligente/runs/detect/train_set2_70_1/weights/best.pt")  # load a custom model

threshold = 0.7

class_name_dict = {0: 'car'}

# Read the image
frame = cv2.imread(image_path)

# Perform object detection
results = model(frame)[0]

# Draw bounding boxes and labels on the image
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
        cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

# Save the output image as JPEG
cv2.imwrite(output_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
