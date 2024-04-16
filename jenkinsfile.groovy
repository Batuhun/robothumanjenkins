pipeline {
    agent {
        docker {
            image 'python:3.10-slim' 
            args '-u root:root'
        }
    }
    triggers {
            pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install ultralytics==8.0.196
                pip install roboflow 
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
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
