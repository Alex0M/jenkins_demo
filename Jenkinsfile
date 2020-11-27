pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    options {
        timestamps()
    }
    stages {
        stage('Build a Docker Image') { 
            steps {
                sh ("docker build -t myapp:dev.${env.BUILD_NUMBER} .")
            }
        }
        stage('Stop docker container') { 
            steps {
                sh ("docker stop myapp")
            }
        }
        stage('Deploy app') { 
            steps {
                sh ("docker run --name=myapp --rm -d -p 8081:5000 myapp:dev.${env.BUILD_NUMBER}")
            }
        }
    }
}