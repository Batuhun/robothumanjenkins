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
                    sh 'apk update && sudo apk add docker'

                    // Install Python
                    sh 'apk add python3'
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
