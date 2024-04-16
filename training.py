from ultralytics import YOLO
from roboflow import Roboflow


rf = Roboflow(api_key="tcoKTgvDJQbxwi8pIzeg")
project = rf.workspace("robot-human-detection").project("robot-human-detection")
version = project.version(1)
dataset = version.download("yolov8")

print(dataset.location+"/data.yaml")

model = YOLO("yolov8l.yaml")  # build a new model from scratch
model = YOLO("yolov8l.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data=dataset.location+"/data.yaml", epochs=1,imgsz=640)
metrics = model.val()