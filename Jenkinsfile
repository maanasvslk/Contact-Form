pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/maanasvslk/maanasvslk-contact-form.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t maanasvslk-contact-form:latest .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker stop contact-web || true'
                sh 'docker rm contact-web || true'
                sh 'docker run -d -p 80:5000 -v $(pwd)/contacts.db:/app/contacts.db --name contact-web maanasvslk-contact-form:latest'
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