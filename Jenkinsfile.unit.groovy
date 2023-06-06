pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/oscarsaavedra06/unir-test'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
         stage('Api tests') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        } 
        //  failure {  
        //      mail bcc: '', body: "<b>Fallo en</b><br>Project: ${env.JOB_NAME} <br>Número de ejecucion: ${env.BUILD_NUMBER}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "correo@correo.com";  
        //  }
        failure {  
             echo "Fallo en Project: ${env.JOB_NAME} Número de ejecucion: ${env.BUILD_NUMBER}"
         }    
    
    }
}

