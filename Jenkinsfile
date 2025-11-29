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
               
                bat 'docker compose run --rm --user 0 backend sh -c "cd /app/Backend && PYTHONPATH=. python -m coverage run --source=. --data-file=.coverage.ci tests/run_tests.py && coverage xml -o /app/Backend/coverage.xml --data-file=.coverage.ci"'
            }
        }

        stage('Ejecutar pruebas + coverage') {
            steps {
                echo "Ejecutando pruebas y generando reporte de cobertura..."
                
                bat 'docker compose run --rm --user 0 backend sh -c "cd /app/Backend && PYTHONPATH=. python -m coverage run --source=. --data-file=.coverage.ci tests/run_tests.py && coverage xml -o /tmp/coverage.xml --data-file=.coverage.ci && mv /tmp/coverage.xml ."'
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
            // Limpia los contenedores en caso de fallo, pero los mantiene si el despliegue es exitoso (stage final)
            // Se usa 'if (currentBuild.result == 'FAILURE')' para asegurar que el 'up -d' del final no sea interrumpido.
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