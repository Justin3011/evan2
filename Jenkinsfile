pipeline {
    agent any

    stages {
        stage('Limpiar contenedor') {
            steps {
                sh 'docker stop api-eva2 || true'
                sh 'docker rm api-eva2 || true'
                sh 'docker rmi fastapi-eva2 || true'
            }
        }
        stage('Construir imagen') {
            steps {
                sh 'docker build -t fastapi-eva2 .'
            }
        }
        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run -d -p 8000:8000 --name api-eva2 fastapi-eva2'
            }
        }
    }
}
