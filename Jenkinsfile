pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                echo "Clonando repositorio..."
                git branch: 'main',
                    url: 'https://github.com/Dfelirojas/Proyecto-CI.git'
            }
        }

        stage('Construir contenedores') {
            steps {
                echo "Construyendo contenedores Docker..."
                bat 'docker compose build'
            }
        }

       stage('Ejecutar pruebas + coverage') {
            steps {
                echo "Ejecutando pruebas y generando reporte de cobertura..."
                // 1. Ejecuta pruebas, genera datos en .coverage-data y copia el reporte XML a .coverage-report.xml
                bat 'docker compose run --rm --user 0 backend sh -c "cd /app/Backend && PYTHONPATH=. python -m coverage run --source=. --data-file=.coverage-data tests/run_tests.py && coverage xml -o /tmp/coverage.xml --data-file=.coverage-data && cp /tmp/coverage.xml .coverage-report.xml"'

                echo "Copiando reporte de cobertura del contenedor al workspace del Host..." 
                bat 'FOR /F %%i IN ("docker compose ps -q backend") DO docker cp %%i:/app/Backend/.coverage-report.xml .'
                
                echo "Subiendo reporte a Codecov de forma segura..."
                // 2. Inyecta la credencial secreta CODECOV_TOKEN_ID en la variable de entorno CODECOV_TOKEN
                withCredentials([string(credentialsId: 'CODECOV_TOKEN_ID', variable: 'CODECOV_TOKEN')]) {
                    // 3. Descarga el uploader de Codecov para Windows
                    bat 'curl -Os https://uploader.codecov.io/latest/codecov.exe'
                
                    // 4. Sube el reporte. El -t %CODECOV_TOKEN% usa el token inyectado de forma segura.
                    bat 'codecov.exe -t %CODECOV_TOKEN% -f .coverage-report.xml'
                }
            }
        }
        
        stage('Desplegar entorno final') {
            steps {
                echo "Desplegando la aplicación con Docker Compose..."
                bat 'docker compose up -d --build'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo "Pipeline ejecutado correctamente. Aplicación desplegada."
        }
        failure {
            echo "Error en el pipeline. Deteniendo contenedores."
            // Detiene y elimina los contenedores creados si hay un fallo
            bat 'docker compose down --remove-orphans'
        }
    }
}