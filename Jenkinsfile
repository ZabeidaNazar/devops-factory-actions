pipeline {
    agent any
    
    // Use the managed Terraform installation
    tools {
        terraform 'terraform-1.15.8'
    }

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'pwd'
            }
        }

        stage('Tools validation') {
            steps {
                sh 'terraform version'
            }
        }

        stage('Init') {
            steps {
                dir('terraform') {
                    // terraform is now available on PATH
                    sh 'terraform version'
                    sh 'terraform init -input=false'
                }
            }
        }
    }
}
