def is_container_exist = false
def appname = "myapp"
def container_name = "myapp-dev"
def version = "dev"

pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    options {
        timestamps()
    }
    stages {
        stage('Build a Docker Image') { 
            steps {
                sh ("docker build -t ${appname}:${version}.${env.BUILD_NUMBER} .")
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
                    is_run = sh(script: """ [ "\$(docker ps -q -f name=${appname})" ] && echo yes || echo no """, returnStdout: true)
                    if (is_run.trim() == "yes") {
                        is_container_exist = true
                    }
                }
            }
        }

        stage('Stop docker container') {
            when { expression { is_container_exist == true } }
            steps {
                sh ("docker stop ${appname}")
            }
        }

        stage('Deploy app') { 
            steps {
                sh ("docker run --name=${container_name} --rm -d -p 8081:5000 ${appname}:${version}.${env.BUILD_NUMBER}")
            }
        }
    }
}