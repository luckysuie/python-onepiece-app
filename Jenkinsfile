pipeline{
    agent any
    stages{
        stage("Git checkout"){
            steps{
                echo "Cloniing the Pythonn project source code from the GitHub repository"
                git branch: 'main', url: 'https://github.com/luckysuie/python-onepiece-app'
            }
        }
        stage("pythonn buuild"){
            steps{
                echo "Building the Python application"
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage("Python test"){   
            steps{
                echo "Running tests for the Python application"
                sh '''
                . venv/bin/activate
                pytest app/tests/test_app.py
                '''
            }
        stage("Docker build and push"){
            steps{
                echo "Building and Pushing the Docker image to Docker Hub"
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]){
                    sh '''
                    echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin
                    docker build -t luckysuie/python-onepiece-app:latest .
                    docker push luckysuie/python-onepiece-app:latest
                    '''
                }
            }
        }
    }
}