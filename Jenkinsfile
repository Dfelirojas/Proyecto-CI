pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dfelirojas/Proyecto-CI.git'
            }
        }

        stage('Construir contenedores') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Ejecutar pruebas + coverage') {
            steps {
                // 1. Ejecuta el script de pruebas usando la ruta absoluta verificada: /app/Backend/tests/run_tests.py
                bat 'docker compose run --rm backend sh -c "PYTHONPATH=/app/Backend python -m coverage run --source=/app/Backend /app/Backend/tests/run_tests.py"'

                // 2. Genera el archivo coverage.xml. (Se debe generar en el directorio del código fuente)
                bat 'docker compose run --rm backend sh -c "cd /app/Backend && coverage xml -o coverage.xml"'
            }
        }

        stage('Enviar a Codecov') {
            steps {
                // Comando para el uploader de Codecov en Windows
                bat '''
                    curl -Os https://uploader.codecov.io/latest/windows/codecov.exe
                    codecov.exe -f coverage.xml
                '''
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
            echo "Pipeline ejecutado correctamente."
        }
        failure {
            echo "Error en el pipeline."
            bat 'docker compose down --remove-orphans'
        }
    }
}