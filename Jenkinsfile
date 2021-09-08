pipeline {
    agent none
    stages {
        stage('Test on Python3.6') {
            agent { docker { image '3.6.15-alpine3.13' } }
            steps {
                sh 'python --version'
            }
        }
        stage('Test on Python3.7') {
            agent { docker { image '3.7.12-alpine3.13' } }
            steps {
                sh 'python --version'
            }
        }
        stage('Test on Python3.8') {
            agent { docker { image '3.8.12-alpine3.13' } }
            steps {
                sh 'python --version'
            }
        }
        stage('Test on Python3.9') {
            agent { docker { image '3.6.15-alpine3.13' } }
            steps {
                sh 'python --version'
            }
        }
        stage('Test on Python3.10rc2') {
            agent { docker { image '3.10rc2-alpine3.13' } }
            steps {
                sh 'python --version'
            }
        }
    }
}