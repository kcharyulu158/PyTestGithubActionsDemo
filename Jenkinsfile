pipeline {
    agent any

    // Ensure Docker commands can run natively on the Jenkins agent
    options {
        timeout(time: 30, unit: 'MINUTES')
       //ansiColor('xterm')
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls code from your GitHub repository automatically
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Selenium Python execution container...'
                    // Compiles your Dockerfile from the project root
                    // Make sure your Dockerfile is set to use the headless browser configuration
                    app = docker.build("selenium-tests:${BUILD_NUMBER}", ".")
                }
            }
        }

        stage('Execute Selenium Tests') {
            steps {
                script {
                    echo 'Running Pytest Suite inside the Docker container...'
                    // Runs the container and mounts the workspace reports folder 
                    // This extracts the report.html back to Jenkins before the container dies
                    app.inside("-v ${WORKSPACE}/reports:/app/reports") {
                        sh 'python -m pytest'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Publishing HTML Test Reports...'
            // Uses HTML Publisher plugin to display the interactive framework report directly inside Jenkins
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
                // Clean up the image to prevent your Jenkins server hard drive from filling up
                sh "docker rmi selenium-tests:${BUILD_NUMBER} || true"
            }
        }
    }
}
