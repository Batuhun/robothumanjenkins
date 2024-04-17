from ultralytics import YOLO
from roboflow import Roboflow
import os
import zipfile

rf = Roboflow(api_key="tcoKTgvDJQbxwi8pIzeg")
project = rf.workspace("robot-human-detection").project("robot-human-detection")
version = project.version(1)
dataset = version.download("yolov8")

try:
    with zipfile.ZipFile('/var/jenkins_home/workspace/RobotHumanYOLOv8/robot-human-detection-1/roboflow.zip', 'r') as zip_ref:
        zip_ref.extractall('/var/jenkins_home/workspace/RobotHumanYOLOv8/robot-human-detection-1')
except:
    print('error unzipping')

print(os.listdir("/var/jenkins_home/workspace/"))
print('\n')
print(os.listdir("/var/jenkins_home/workspace/RobotHumanYOLOv8/"))
print('\n')
print(os.listdir("/var/jenkins_home/RobotHumanYOLOv8/robot-human-detection-1"))

filename = "/var/jenkins_home/workspace/RobotHumanYOLOv8/robot-human-detection-1/data.yaml"
with open(filename, "r") as f:
    lines = f.readlines()
with open(filename, "w") as f:
    for line in lines:
        if line.strip("\n")[0:3] == "tra":
            f.write('train: train/images\n')
        elif line.strip("\n")[0:3] == "val":
            f.write('val: valid/images\n')
        else:
          f.write(line)
f = open("/content/robot-human-detection-1/data.yaml", "r")
print('----------\n')
print(f.read())

model = YOLO("yolov8l.yaml")  # build a new model from scratch
model = YOLO("yolov8l.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data=dataset.location+"/data.yaml", epochs=1,imgsz=640)
metrics = model.val()