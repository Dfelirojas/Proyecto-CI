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

        stage('Levantar contenedores (pruebas)') {
            steps {
                bat 'docker compose up -d --build --force-recreate'
            }
        }

        stage('Ejecutar Pruebas') { 
            steps {
                bat 'docker compose run --rm backend python -m unittest discover'
            }
        }

        stage('Destruir contenedores anteriores y reconstruir para despliegue') {
            steps {
                bat 'docker compose down --remove-orphans'
                bat 'docker compose up -d --build'
            }
        }

        stage('Desplegar') {
            steps {
                echo "Despliegue finalizado y contenedores funcionando."
            }
        }
    }

    post {
        success {
            echo "Pipeline ejecutado correctamente."
        }
        failure {
            echo "Error en el pipeline."
            // Opcional: limpieza automática en caso de fallo
            bat 'docker compose down --remove-orphans'
        }
    }
}

