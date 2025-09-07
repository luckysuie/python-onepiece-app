#!/usr/bin/env bash
set -euo pipefail

echo "=== Updating system packages ==="
sudo apt-get update -y
sudo apt-get upgrade -y

echo "=== Installing core dependencies (Python, build tools, git) ==="
sudo apt-get install -y python3 python3-venv python3-pip git build-essential python3-dev unixodbc-dev curl

echo "=== Installing Microsoft ODBC Driver 18 for SQL Server ==="
if ! dpkg -s msodbcsql18 >/dev/null 2>&1; then
  curl -fsSL https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -o packages-microsoft-prod.deb
  sudo dpkg -i packages-microsoft-prod.deb
  sudo apt-get update -y
  sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
  rm -f packages-microsoft-prod.deb
else
  echo "ODBC Driver 18 already installed."
fi

echo "=== Setting up Python virtual environment ==="
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pip

echo "=== Installing Python requirements ==="
pip install -r requirements.txt

echo "=== Creating uploads directory if missing ==="
mkdir -p uploads

echo "=== Setup complete! ==="
echo ""
echo "Next steps:"
echo "1. Activate the venv:  source .venv/bin/activate"
echo "2. Run the app:        uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"
echo ""
echo "Your app should now be accessible on: http://<VM_PUBLIC_IP>:8000/"
