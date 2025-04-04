pipeline {
    agent any
    // Disable the default SCM checkout
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Checkout Code') {
            steps {
                // Explicitly clean the workspace before checkout
                deleteDir()
                git branch: 'main',
                    url: 'https://github.com/maanasvslk/Contact-Form.git',
                    credentialsId: 'git_id'
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