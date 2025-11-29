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

        stage('Construir contenedores') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Ejecutar pruebas + coverage') {
            steps {
                // Ejecuta pruebas con coverage dentro del contenedor backend
                bat 'docker compose run --rm backend coverage run -m unittest discover'

                // Genera el archivo coverage.xml
                bat 'docker compose run --rm backend coverage xml -o coverage.xml'

                // Copia el coverage.xml al workspace de Jenkins
                bat 'docker cp juego_backend:/app/coverage.xml coverage.xml'
            }
        }

        stage('Enviar a Codecov') {
            steps {
                withCredentials([string(credentialsId: 'codecov-token', variable: 'CODECOV_TOKEN')]) {
                    bat '''
                        curl -Os https://uploader.codecov.io/latest/windows/codecov.exe
                        codecov.exe -t %CODECOV_TOKEN% -f coverage.xml
                    '''
                }
            }
        }

        stage('Desplegar entorno final') {
            steps {
                bat 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo "✔ Pipeline ejecutado correctamente."
        }
        failure {
            echo "Error en el pipeline."
            bat 'docker compose down --remove-orphans'
        }
    }
}
