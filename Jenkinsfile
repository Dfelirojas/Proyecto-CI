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
                bat 'docker compose run --name ci_backend_test --user 0 backend sh -c "cd /app/Backend && PYTHONPATH=. python -m coverage run --source=. --data-file=.coverage-data tests/run_tests.py && coverage xml -o /tmp/coverage.xml --data-file=.coverage-data && cp /tmp/coverage.xml .coverage-report.xml"'
                
                echo "Copiando reporte de cobertura del contenedor al workspace del Host..."
                bat 'docker cp ci_backend_test:/app/Backend/.coverage-report.xml .'
                
                echo "Limpiando contenedor de pruebas..."
                bat 'docker rm ci_backend_test'
                
                echo "Subiendo reporte a Codecov de forma segura..."
                withCredentials([string(credentialsId: 'CODECOV_TOKEN_ID', variable: 'CODECOV_TOKEN')]) {
                    bat 'curl -Os https://uploader.codecov.io/latest/codecov.exe'
                
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
            bat 'docker compose down --remove-orphans' 
        }
    }
}