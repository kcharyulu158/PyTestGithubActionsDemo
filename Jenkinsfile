pipeline {
    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Selenium Python execution container on Windows...'
                    // Windows uses standard batch execution strings rather than 'sh'
                    bat "docker build -t selenium-tests:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Execute Selenium Tests') {
            steps {
                script {
                    echo 'Running Pytest Suite inside the Docker container...'
                    // Maps Windows paths cleanly using forward slashes or standard quotes
                    bat "docker run --rm -v \"%WORKSPACE%/reports:/app/reports\" selenium-tests:${BUILD_NUMBER}"
                }
            }
        }
    }

    post {
        always {
            echo 'Publishing HTML Test Reports...'
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Selenium Pytest Report',
                reportTitles: "Build #${BUILD_NUMBER} Matrix"
            ])
            
            echo 'Cleaning up system Docker images...'
            script {
                // The 'exit 0' catch ensures the pipeline finishes cleanly even if the image wasn't built
                bat "docker rmi selenium-tests:${BUILD_NUMBER} || exit 0"
            }
        }
    }
}
