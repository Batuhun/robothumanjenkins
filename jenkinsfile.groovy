pipeline {
    agent { 
        node {
            label 'agent1'
            }
      }
    triggers {
            pollSCM '* * * * *'
    }
    stages {
        stage('Install Docker and Python') {
            steps {
                    // Install Docker
                    sh 'apt-get update && sudo apt-get install -y docker.io'

                    // Install Python
                    sh 'apt-get install -y python3'
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                docker
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff.."
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
