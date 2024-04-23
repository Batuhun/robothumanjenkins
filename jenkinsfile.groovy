 pipeline {
    agent {
        docker {
            image 'python:3.10-slim' 
            args '-u root:root'
        }
    }
    parameters {
  string defaultValue: '0.0001,0.001,0.01', name: 'learning_rates', trim: true
  string defaultValue: '32,64,128', name: 'batch_sizes', trim: true
  string defaultValue: 'Adam,SGD,AdamW', name: 'optimizers', trim: true
  string defaultValue: '30,50,150', name: 'epochs', trim: true
  string defaultValue: 'yolov8n,yolov8m', name: 'network_architectures', trim: true
  string defaultValue: '0.0,0.2,0.4', name: 'dropout', trim: true
  string defaultValue: '640', name: 'imszg', trim: true
  string defaultValue: 'tcoKTgvDJQbxwi8pIzeg', name: 'dataset_api', trim: true
  string defaultValue: 'Dollar-Bill-Detection', name: 'dataset_name', trim: true
  string defaultValue: '24', name: 'versiom', trim: true
  string defaultValue: 'alex-hyams-cosqx', name: 'workspace', trim: true

    }
    triggers {
            pollSCM '* * * * *'
    }
    stages {
        stage('Enviroment setup') {
            steps {
                echo "Enviroment setup.."
                sh '''
                pip install zipfile36
                pip install ultralytics==8.0.196
                pip install roboflow 
                '''
            }
        }
        stage('Training') {
            steps {
                echo "Training.."
                sh '''
                python3 training.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
