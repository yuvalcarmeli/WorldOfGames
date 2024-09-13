pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'yuvalcarmeli/flask_project:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${env.DOCKER_USERNAME}/flask_project:latest")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${env.DOCKER_USERNAME}/flask-app:latest").inside {
                        sh 'pip install pytest'
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo ${env.DOCKER_PASSWORD} | docker login -u ${env.DOCKER_USERNAME} --password-stdin"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.image("${env.DOCKER_USERNAME}/flask-app:latest").push('latest')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sshagent(['ssh-private-key']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no ${env.SERVER_USER}@${env.SERVER_IP} 'docker pull ${env.DOCKER_USERNAME}/flask-app:latest && docker run -d -p 80:5000 ${env.DOCKER_USERNAME}/flask-app:latest'
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
