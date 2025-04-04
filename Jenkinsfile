pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Explicitly specify credentials if the repo is private
                git branch: 'main',
                    url: 'https://github.com/maanasvslk/Contact-Form.git',
                    credentialsId: 'git_id' // Replace with your Jenkins credential ID
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
                sh 'docker run -d -p 80:5000 -v contacts-db:/app/data --name contact-web maanasvslk-contact-form:latest'
            }
        }
    }
    post {
        always {
            // Wrap the sh step in a node block to ensure workspace context
            node('') {
                sh 'docker image prune -f'
            }
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}