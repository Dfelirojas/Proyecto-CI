pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dfelirojas/Proyecto-CI.git'
            }
        }

        stage('Construir contenedores Docker') {
            steps {
                bat 'docker compose build'
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


