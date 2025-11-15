pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dfelirojas/Proyecto-CI.git',
                    credentialsId: '89b690d6-5a8b-4c2a-890e-7d0be95f8b77'
            }
        }

        stage('Construir contenedores Docker') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Levantar contenedores') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Ejecutar Pruebas') { 
            steps {
                bat 'docker compose run --rm backend python -m unittest discover'
            }
        }

        stage('Desplegar') {
            steps {
                bat 'docker compose up -d'
            }
        }
    }

    post {
        success {
            echo "Pipeline ejecutado correctamente."
        }
        failure {
            echo "Error en el pipeline."
        }
    }
}



