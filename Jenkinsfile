pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t maanasvslk-contact-form:latest .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker stop contact-web || true'
                sh 'docker rm contact-web || true'
                sh 'docker run -d -p 80:5000 -v contacts-db:/app/data --name contact-web maanasvslk-contact-form:latest'
            }
        }
    }
    post {
        always {
            sh 'docker image prune -f'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}