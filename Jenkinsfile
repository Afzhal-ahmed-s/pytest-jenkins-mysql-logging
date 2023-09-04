pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                script {
                    // Check if Python 3.9 is already installed
                    def installed = sh(script: 'python3.9 --version', returnStatus: true)

                    if (installed == 0) {
                        echo "Python 3.9 is already installed"
                    } else {
                        echo "Installing Python 3.9..."

                        // Add a repository for Python 3.9 if needed (for Debian/Ubuntu)
                        sh 'sudo add-apt-repository ppa:deadsnakes/ppa -y'
                        sh 'sudo apt-get update'

                        // Install Python 3.9 (for Debian/Ubuntu)
                        sh 'sudo apt-get install python3.9 -y'
                    }
                }
            }
        }

        stage('Check Python Version') {
            steps {
                // Verify the installed Python version
                sh 'python3.9 --version'
            }
        }

        stage('Run Python code') {
            steps {
                // Run your pytest code
                sh '/home/afzhal-ahmed-s/pytest-jenkins-mysql-logging/pycharm_projects/task/args_kwargs_2.py'
            }
        }
    }

    post {
        success {
            echo "Python 3.9 installation successful"
        }
        failure {
            error "Python 3.9 installation failed"
        }
    }

}
