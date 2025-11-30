🎮 Juego Matemático

Proyecto en desarrollo con arquitectura Frontend (Nginx/HTML/JS) + Backend (Flask/Python).

🏗️ Estado actual

Fase De Pruebas (CI/CD funcional): La tubería de Jenkins automatiza la construcción, pruebas unitarias y despliegue continuo de la aplicación.

🚀 Cómo ejecuta el proyecto

Para levantar la aplicación localmente o para iniciar el flujo de Integración Continua (CI):

1. Ejecución Local

Construir las imágenes y levantar los contenedores en segundo plano. Esto incluye la configuración del Reverse Proxy (Nginx) para que el Frontend se comunique con el Backend.

docker compose up -d --build


Acceso: La aplicación estará disponible en http://localhost:8081.

2. Flujo de Integración Continua (Jenkins)

El pipeline se ejecuta automáticamente tras un git push y se encarga de:

Construir Contenedores: Reconstruye las imágenes, forzando la actualización de la configuración de Nginx.

Ejecutar Pruebas: Inicia un contenedor de prueba temporal (backend) para ejecutar las pruebas unitarias y generar el reporte de cobertura.

Despliegue: Despliega la nueva versión de los contenedores si las pruebas son exitosas.

3. Reporte de Cobertura (Codecov)

Después de que las pruebas unitarias finalizan con éxito en Jenkins:

El reporte de cobertura se copia del contenedor al workspace de Jenkins.

Un script de Bash sube el archivo de reporte a la plataforma Codecov para su visualización y análisis.