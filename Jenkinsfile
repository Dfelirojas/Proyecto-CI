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

        stage('Construir imágenes Docker') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat 'docker compose up --build --exit-code-from backend --abort-on-container-exit'
            }
        }

        stage('Limpiar contenedores de pruebas') {
            steps {
                bat 'docker compose down --remove-orphans'
            }
        }

        stage('Desplegar entorno final') {
            steps {
                bat 'docker compose up -d --build'
                echo "Despliegue completado exitosamente 🚀"
            }
        }
    }

    post {
        success {
            echo "Pipeline ejecutado correctamente 😎"
        }
        failure {
            echo "Error detectado, limpiar contenedores"
            bat 'docker compose down --remove-orphans'
        }
    }
}


