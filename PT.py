from ultralytics import YOLO
import cv2

model = YOLO("D:/estacionamento_inteligente/runs/detect/train-500epochs/weights/best.pt")
frame_skip = 5  # Skip detection on every 3rd frame

video_path = "C:/Users/dani/Desktop/videos_davi/DJI_0270.MP4"
cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()
frame_count = 0

while ret:
    frame_count += 1

    if frame_count % frame_skip == 0:
        results = model.predict(frame, show=True,conf = 0.75,line_width = 1,device=0)

        # Process the detection results as needed
        for result in results:
            # Access the bounding box information and perform further processing
            pass

    # Display or save the frame
    cv2.waitKey(1)

    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()