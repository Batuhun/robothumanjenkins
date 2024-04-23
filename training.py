from ultralytics import YOLO
from roboflow import Roboflow
import os
import zipfile
from sklearn.model_selection import ParameterGrid

avg_res=0.0
learning_rates = [float(x) for x in os.getenv("learning_rates").split(',')]
batch_sizes = [int(x) for x in os.getenv("batch_sizes").split(',')]
optimizers = os.getenv("optimizers").split(',')
epochs = [int(x) for x in os.getenv("epochs").split(',')]
network_architectures = os.getenv("network_architectures").split(',')
dropout = [float(x) for x in os.getenv("dropout").split(',')]
imgsz = int(os.getenv("imgsz"))
dataset_api = os.getenv("dataset_api")
dataset_name = os.getenv("dataset_name")
version = int(os.getenv("version"))
workspace = os.getenv("workspace")
average_result_value = float(os.getenv("average_result_value"))

rf = Roboflow(api_key=dataset_api)
project = rf.workspace(workspace).project(dataset_name.lower())#dataset névtől függ mit kell kibontani
version = project.version(version)
dataset = version.download("yolov8")

try:
    with zipfile.ZipFile('/var/jenkins_home/workspace/RobotHumanYOLOv8/'+dataset_name+'-'+str(version)+'/roboflow.zip', 'r') as zip_ref:
        zip_ref.extractall('/var/jenkins_home/workspace/RobotHumanYOLOv8/'+dataset_name+'-'+str(version))
except:
    print('error unzipping')


filename = '/var/jenkins_home/workspace/RobotHumanYOLOv8/'+dataset_name+'-'+str(version)+'/data.yaml'
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

# Set up the search space
search_space = {'learning_rate': learning_rates,
                'batch_size': batch_sizes,
                'optimizer': optimizers,
                'epochs': epochs,
                'network_architecture': network_architectures,
                'dropout': dropout}

# Create parameter grid
parameter_grid = ParameterGrid(search_space)

# Train and evaluate the model for each combination of hyperparameters
for parameters in parameter_grid:
    # Set hyperparameters for the model
    learning_rate = parameters['learning_rate']
    batch_size = parameters['batch_size']
    optimizer = parameters['optimizer']
    num_epochs = parameters['epochs']
    architecture = parameters['network_architecture']
    dropout = parameters['dropout']

    
    
    model = YOLO(architecture+".yaml")  # build a new model from scratch
    model = YOLO(architecture+".pt")  # load a pretrained model (recommended for training)

    # Train and evaluate the model
    model.train(data=dataset.location+"/data.yaml",epochs=num_epochs ,imgsz=imgsz,lr0=learning_rate,batch=batch_size, optimizer=optimizer, dropout=dropout)
    metrics = model.val()
    print(metrics.results_dict)

    
    # Save the results
    if(metrics.results_dict.get(('metrics/precision(B)')+ metrics.results_dict.get('metrics/recall(B)')+ metrics.results_dict.get('metrics/mAP50(B)')+ metrics.results_dict.get('metrics/mAP50-95(B)')+ metrics.results_dict.get('fitness'))/5>avg_res):
        result = {'learning_rate': learning_rate,
                'batch_size': batch_size,
                'optimizer': optimizer,
                'num_epochs': num_epochs,
                'architecture': architecture,
                'dropout': dropout}
        avg_res=metrics.results_dict.get(('metrics/precision(B)')+ metrics.results_dict.get('metrics/recall(B)')+ metrics.results_dict.get('metrics/mAP50(B)')+ metrics.results_dict.get('metrics/mAP50-95(B)')+ metrics.results_dict.get('fitness'))/5
    # Stop
    if(metrics.results_dict.get(('metrics/precision(B)')+ metrics.results_dict.get('metrics/recall(B)')+ metrics.results_dict.get('metrics/mAP50(B)')+ metrics.results_dict.get('metrics/mAP50-95(B)')+ metrics.results_dict.get('fitness'))/5>average_result_value):
        break

print(result)

