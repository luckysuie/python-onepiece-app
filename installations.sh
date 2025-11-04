#!/bin/bash
sudo apt update -y
wget -O docker.sh https://get.docker.com/
sudo sh docker.sh
sudo usermod -aG docker jenkins
sudo usermod -aG docker $USER
sudo systemctl restart docker
sudo systemctl restart jenkins
newgrp docker
