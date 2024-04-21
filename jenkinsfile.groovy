 pipeline {
    agent {
        docker {
            image 'python:3.10-slim' 
            args '-u root:root'
        }
    }
    parameters {
  text defaultValue: 'alma fa', description: 'leírás valami', name: 'parameters'
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
