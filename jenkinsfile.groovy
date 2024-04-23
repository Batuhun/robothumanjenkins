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
    }
    triggers {
            pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
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
