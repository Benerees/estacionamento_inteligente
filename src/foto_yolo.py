import os
import cv2
from ultralytics import YOLO

image_path = 'C:/Users/dani/Documents/istockphoto-856857870-612x612.jpg'
output_path = 'D:/estacionamento_inteligente/data/foto.JPG'

model = YOLO("D:/estacionamento_inteligente/runs/detect/30m/30m_1/weights/best.pt")  # load a custom model

threshold = 0.3

class_name_dict = {0: 'car'}


frame = cv2.imread(image_path)

results = model(frame)[0]

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
        cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.1, (0, 255, 0), 1, cv2.LINE_AA)

cv2.imwrite(output_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
