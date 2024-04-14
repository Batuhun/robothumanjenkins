pipeline {
    agent { 
        dockerfile true
      }
    triggers {
            pollSCM '* * * * *'
    }
    stages {
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
