pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/mlops-jenkins-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python src/train.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh 'python src/evaluate.py'
            }
        }

        stage('Check Accuracy & Retrain') {
            steps {
                script {
                    def acc = sh(script: "python utils/get_accuracy.py", returnStdout: true).trim()
                    if (acc.toFloat() < 0.75) {
                        sh 'python src/train.py'
                    }
                }
            }
        }

        stage('Data Drift Detection') {
            steps {
                sh 'python monitoring/drift.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 mlops-app'
            }
        }
    }
}