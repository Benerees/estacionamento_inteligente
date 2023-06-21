import os
import cv2
from ultralytics import YOLO

image_path = 'D:/estacionamento_inteligente/data/images/val/ocupadas_set1_50m_1.JPG'
output_path = 'D:/estacionamento_inteligente/data/result.JPEG'

model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

# Load the model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

class_name_dict = {0: 'car'}

# Read the image
frame = cv2.imread(image_path)

# Perform object detection
results = model(frame)[0]

# Draw bounding boxes and labels on the image
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# Save the output image as JPEG
cv2.imwrite(output_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
