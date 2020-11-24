pipeline {
    agent any
    options {
        timestamp()
    }
    stages {
        stage('Build a Docker Image') { 
            steps {
                sh ("docker build -t myapp:dev.${env.BUILD_NUMBER} .")
            }
        }
        stage('Deploy app') { 
            steps {
                sh ("docker run --name=myapp --rm -d -p 8081:5000 myapp:dev.${env.BUILD_NUMBER}")
            }
        }
    }
}