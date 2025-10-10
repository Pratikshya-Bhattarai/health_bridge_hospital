#!/bin/bash

# HealthBridge Hospital - PythonAnywhere Deployment Script
# This script automates the deployment process to PythonAnywhere

set -e  # Exit on any error

echo "🚀 Starting HealthBridge Hospital Deployment to PythonAnywhere..."

# Configuration
PYTHONANYWHERE_USERNAME="pratikshyabhattarai"
PYTHONANYWHERE_HOST="pythonanywhere.com"
PROJECT_NAME="health_bridge_hospital"
BACKEND_DIR="backend"

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

# Check if SSH key exists
if [ ! -f ~/.ssh/pythonanywhere_key ]; then
    print_warning "SSH key not found. Generating new SSH key..."
    ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f ~/.ssh/pythonanywhere_key -N ""
    print_success "SSH key generated successfully"
    print_warning "Please add the public key to PythonAnywhere:"
    echo "Public key:"
    cat ~/.ssh/pythonanywhere_key.pub
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

# Deploy to PythonAnywhere
print_status "Deploying to PythonAnywhere..."

ssh ${PYTHONANYWHERE_USERNAME}@${PYTHONANYWHERE_HOST} << 'EOF'
    set -e
    
    # Navigate to project directory
    cd /home/pratikshyabhattarai/health_bridge_hospital
    
    # Pull latest changes
    echo "📥 Pulling latest changes from GitHub..."
    git pull origin main
    
    # Navigate to backend
    cd backend
    
    # Activate virtual environment
    echo "🐍 Activating virtual environment..."
    source venv/bin/activate
    
    # Install/update dependencies
    echo "📦 Installing dependencies..."
    pip install --user -r requirements.txt
    
    # Run database migrations
    echo "🗄️ Running database migrations..."
    python manage.py migrate --settings=healthbridge_backend.settings_production
    
    # Collect static files
    echo "📁 Collecting static files..."
    python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
    
    # Create logs directory if it doesn't exist
    mkdir -p logs
    
    # Restart web application
    echo "🔄 Restarting web application..."
    touch /var/www/bepratikshya_pythonanywhere_com_wsgi.py
    
    echo "✅ Deployment completed successfully!"
EOF

if [ $? -eq 0 ]; then
    print_success "Deployment completed successfully!"
    print_status "Your application is now live at: https://pratikshyabhattarai.pythonanywhere.com"
    print_status "API endpoint: https://pratikshyabhattarai.pythonanywhere.com/api/"
    print_status "Admin panel: https://pratikshyabhattarai.pythonanywhere.com/admin/"
else
    print_error "Deployment failed. Please check the error messages above."
    exit 1
fi
