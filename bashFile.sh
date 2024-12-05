pip install flask flask-sqlalchemy flask-jwt-extended
#!/bin/bash

# Bash script to set up the Flask REST API project

# Step 1: Update and Install Required Packages
echo "Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

# Step 2: Install Python and Pip
echo "Installing Python and Pip..."
sudo apt install python3 python3-pip -y

# Step 3: Set Up a Virtual Environment
echo "Setting up a virtual environment..."
pip3 install virtualenv
virtualenv venv
source venv/bin/activate

# Step 4: Install Python Dependencies
echo "Installing dependencies..."
pip install flask flask-sqlalchemy flask-jwt-extended

# Step 5: Create SQLite Database
echo "Initializing the SQLite database..."
python3 -c "from app import db; db.create_all()"

# Step 6: Run the Flask Application
echo "Starting the Flask application..."
python3 app.py
