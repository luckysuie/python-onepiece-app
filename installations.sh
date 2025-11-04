sudo apt update
sudo apt install openjdk-21-jdk -y
java -version

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl status jenkins


sudo apt update
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az version

sudo apt update
sudo snap install kubectl --classic
kubectl version --client