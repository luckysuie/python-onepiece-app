pipeline{
    agent any
    stages{
        stage("Git checkout"){
            steps{
                echo "Cloniing the Python project source code from the GitHub repository"
                git branch: 'main', url: 'https://github.com/luckysuie/python-onepiece-app'
            }
        }
        stage("pythonn build"){
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
        }
    }
}