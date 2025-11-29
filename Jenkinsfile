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
                // Ejecuta pruebas con coverage. coverage.xml se genera en el host gracias al volumen.
                bat 'docker compose run --rm backend coverage run --source=/app -m unittest discover'

                // Genera el archivo coverage.xml. Este archivo aparecerá en la raíz de tu proyecto.
                bat 'docker compose run --rm backend coverage xml -o coverage.xml'

                // ¡Ya no se necesita el docker cp! El archivo ya está en el workspace.
            }
        }

        stage('Enviar a Codecov') {
            steps {
                // Comando correcto para el uploader de Codecov en Windows (como ya lo tenías)
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
        // ... (El post se mantiene igual)
        success {
            echo "Pipeline ejecutado correctamente."
        }
        failure {
            echo "Error en el pipeline."
            bat 'docker compose down --remove-orphans'
        }
    }
}