pipeline {
    agent none
    stages {
        stage('Test on Python3 on controller') {
            agent any
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pip freeze'
            }
        }
    }
}