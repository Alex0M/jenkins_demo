def is_container_exist = false

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

        stage('Test') {
            steps {
                sleep 3
            }
        }

        stage ('Check if container exist') {
            steps {
                script {
                    is_run = sh(script: """ [ "\$(docker ps -q -f name=myapp)" ] && echo yes || echo no """, returnStdout: true)
                    if (is_run.trim() == "yes") {
                        is_container_exist = true
                    }
                }
            }
        }

        stage('Stop docker container') {
            when { expression { is_container_exist == true } }
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