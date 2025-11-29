pipeline {
    agent any

    environment {
        CODECOV_TOKEN = credentials('codecov-token')   // ID del token en Jenkins
    }

    stages {

        stage('Clonar repositorio') {
            steps {
                git(
                    url: 'https://github.com/Dfelirojas/Proyecto-CI.git',
                    branch: 'main',
                    credentialsId: '89b690d6-5a8b-4c2a-890e-7d0be95f8b77'
                )
            }
        }

        stage('Construir contenedores') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Ejecutar pruebas + coverage') {
            steps {
                // IMPORTANTE: moverse a Backend dentro del contenedor
                bat '''
                docker compose run --rm backend sh -c "cd Backend && \
                    coverage run -m unittest discover -s tests -p 'test_*.py'"
                '''

                bat '''
                docker compose run --rm backend sh -c "cd Backend && \
                    coverage xml -o coverage.xml"
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'Backend/coverage.xml', allowEmptyArchive: true
                }
            }
        }

        stage('Enviar cobertura a Codecov') {
            when {
                expression { fileExists('Backend/coverage.xml') }
            }
            steps {
                bat '''
                curl -Os https://uploader.codecov.io/latest/windows/codecov.exe
                codecov.exe -t %CODECOV_TOKEN% -f Backend/coverage.xml
                '''
            }
        }

        stage('Desplegar entorno final') {
            steps {
                echo "Desplegando aplicación final..."
                bat 'docker compose up -d'
            }
        }
    }

    post {
        failure {
            echo "Error en el pipeline."
            bat 'docker compose down --remove-orphans'
        }
        success {
            echo "Pipeline ejecutado correctamente."
        }
    }
}