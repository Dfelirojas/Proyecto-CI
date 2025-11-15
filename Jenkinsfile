pipeline {
    agent any

    stages {

        stage('Construir contenedores') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Desplegar entorno final') {
            steps {
                bat 'docker compose up -d --build'
            }
        }
    }
}


