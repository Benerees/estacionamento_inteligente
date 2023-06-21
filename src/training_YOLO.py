from ultralytics import YOLO



# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
# Use the model
results = model.train(data="config.yaml", epochs=300)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
