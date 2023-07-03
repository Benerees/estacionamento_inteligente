from ultralytics import YOLO

model = YOLO("yolov8n.yaml")  
model = YOLO("yolov8n.pt")  


results = model.train(data="config.yaml", epochs=100, patience = 50, conf = 0.4)  
metrics = model.val() 

