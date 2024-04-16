from ultralytics import YOLO
from roboflow import Roboflow


rf = Roboflow(api_key="tcoKTgvDJQbxwi8pIzeg")
project = rf.workspace("robot-human-detection").project("robot-human-detection")
version = project.version(1)
dataset = version.download("yolov8")

print(dataset.location+"/data.yaml")