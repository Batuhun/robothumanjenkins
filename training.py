'''from ultralytics import YOLO
from roboflow import Roboflow
import os
import zipfile'''
import sys

def hello(a):
    print ("hello and that's your sum:", a )


a = sys.argv[1]
hello(a)
'''
rf = Roboflow(api_key="tcoKTgvDJQbxwi8pIzeg")
project = rf.workspace("alex-hyams-cosqx").project("dollar-bill-detection")#dataset névtől függ mit kell kibontani
version = project.version(24)
dataset = version.download("yolov8")'''
'''
rf = Roboflow(api_key="tcoKTgvDJQbxwi8pIzeg")
project = rf.workspace("robot-human-detection").project("robot-human-detection")
version = project.version(1)
dataset = version.download("yolov8")
''''''
try:
    with zipfile.ZipFile('/var/jenkins_home/workspace/RobotHumanYOLOv8/Dollar-Bill-Detection-24/roboflow.zip', 'r') as zip_ref:
        zip_ref.extractall('/var/jenkins_home/workspace/RobotHumanYOLOv8/Dollar-Bill-Detection-24')
except:
    print('error unzipping')

print(os.listdir("/var/jenkins_home/workspace/"))
print('\n')
print(os.listdir("/var/jenkins_home/workspace/RobotHumanYOLOv8/"))
print('\n')
print(os.listdir("/var/jenkins_home/workspace/RobotHumanYOLOv8/Dollar-Bill-Detection-24"))

filename = "/var/jenkins_home/workspace/RobotHumanYOLOv8/Dollar-Bill-Detection-24/data.yaml"
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


model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data=dataset.location+"/data.yaml", epochs=1,imgsz=640,batch=4)
metrics = model.val()'''
