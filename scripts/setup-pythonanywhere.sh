#!/bin/bash

# HealthBridge Hospital - PythonAnywhere Initial Setup Script
# This script sets up the initial deployment environment on PythonAnywhere

set -e  # Exit on any error

echo "🏥 Setting up HealthBridge Hospital on PythonAnywhere..."

# Configuration
PYTHONANYWHERE_USERNAME="pratikshyabhattarai"
PYTHONANYWHERE_HOST="pythonanywhere.com"
PROJECT_NAME="health_bridge_hospital"
GITHUB_REPO="https://github.com/yourusername/health_bridge_hospital.git"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [ ! -f "package.json" ] || [ ! -d "backend" ]; then
    print_error "Please run this script from the project root directory"
    exit 1
fi

# Generate SSH key if it doesn't exist
if [ ! -f ~/.ssh/pythonanywhere_key ]; then
    print_status "Generating SSH key for PythonAnywhere..."
    ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f ~/.ssh/pythonanywhere_key -N ""
    print_success "SSH key generated successfully"
    
    print_warning "Please add the following public key to PythonAnywhere:"
    echo "=========================================="
    cat ~/.ssh/pythonanywhere_key.pub
    echo "=========================================="
    echo ""
    print_status "Steps to add SSH key to PythonAnywhere:"
    echo "1. Go to https://www.pythonanywhere.com"
    echo "2. Log in with your account"
    echo "3. Go to Account tab"
    echo "4. Click on 'SSH keys'"
    echo "5. Click 'Add a new key'"
    echo "6. Paste the public key above"
    echo "7. Click 'Add key'"
    echo ""
    read -p "Press Enter after adding the SSH key to PythonAnywhere..."
fi

# Test SSH connection
print_status "Testing SSH connection to PythonAnywhere..."
if ssh -o ConnectTimeout=10 -o BatchMode=yes ${PYTHONANYWHERE_USERNAME}@${PYTHONANYWHERE_HOST} exit 2>/dev/null; then
    print_success "SSH connection successful"
else
    print_error "SSH connection failed. Please check your SSH key setup."
    exit 1
fi

# Setup project on PythonAnywhere
print_status "Setting up project on PythonAnywhere..."

ssh ${PYTHONANYWHERE_USERNAME}@${PYTHONANYWHERE_HOST} << EOF
    set -e
    
    # Create project directory
    echo "📁 Creating project directory..."
    mkdir -p /home/pratikshyabhattarai/health_bridge_hospital
    cd /home/pratikshyabhattarai/health_bridge_hospital
    
    # Clone repository (you'll need to update this with your actual GitHub repo)
    echo "📥 Cloning repository..."
    if [ ! -d ".git" ]; then
        git clone ${GITHUB_REPO} .
    else
        echo "Repository already exists, pulling latest changes..."
        git pull origin main
    fi
    
    # Navigate to backend
    cd backend
    
    # Create virtual environment
    echo "🐍 Creating virtual environment..."
    python3.10 -m venv venv
    source venv/bin/activate
    
    # Install dependencies
    echo "📦 Installing dependencies..."
    pip install --user -r requirements.txt
    
    # Create logs directory
    mkdir -p logs
    
    # Copy environment file
    echo "⚙️ Setting up environment variables..."
    cp env.example .env
    
    echo "✅ Initial setup completed!"
    echo ""
    echo "Next steps:"
    echo "1. Update the .env file with your actual credentials"
    echo "2. Run database migrations"
    echo "3. Create superuser"
    echo "4. Configure web app in PythonAnywhere dashboard"
EOF

if [ $? -eq 0 ]; then
    print_success "Initial setup completed successfully!"
    print_status "Next steps:"
    echo "1. SSH into PythonAnywhere: ssh pratikshyabhattarai@pythonanywhere.com"
    echo "2. Navigate to project: cd /home/pratikshyabhattarai/health_bridge_hospital/backend"
    echo "3. Update .env file with your credentials"
    echo "4. Run: python manage.py migrate --settings=healthbridge_backend.settings_production"
    echo "5. Run: python manage.py createsuperuser --settings=healthbridge_backend.settings_production"
    echo "6. Run: python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production"
    echo "7. Configure web app in PythonAnywhere dashboard"
else
    print_error "Setup failed. Please check the error messages above."
    exit 1
fi