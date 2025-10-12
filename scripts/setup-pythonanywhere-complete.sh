#!/bin/bash

# HealthBridge Hospital - Complete PythonAnywhere Setup Script
# This script sets up the backend on PythonAnywhere

echo "🚀 Starting HealthBridge Hospital Backend Setup on PythonAnywhere..."

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
if [ ! -f "manage.py" ]; then
    print_error "Please run this script from the backend directory"
    exit 1
fi

print_status "Setting up HealthBridge Hospital Backend..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_status "Creating virtual environment..."
    python3.10 -m venv venv
    print_success "Virtual environment created"
else
    print_status "Virtual environment already exists"
fi

# Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Install requirements
print_status "Installing Python dependencies..."
pip install --user -r requirements.txt

# Create logs directory
print_status "Creating logs directory..."
mkdir -p logs

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    print_status "Creating .env file from template..."
    cp env.example .env
    print_warning "Please update .env file with your actual configuration values"
else
    print_status ".env file already exists"
fi

# Run database migrations
print_status "Running database migrations..."
python manage.py migrate --settings=healthbridge_backend.settings_production

# Collect static files
print_status "Collecting static files..."
python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production

# Create superuser (optional)
print_status "Creating superuser..."
echo "Do you want to create a superuser? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py createsuperuser --settings=healthbridge_backend.settings_production
fi

# Test Django setup
print_status "Testing Django configuration..."
python manage.py check --settings=healthbridge_backend.settings_production

if [ $? -eq 0 ]; then
    print_success "Django configuration is valid"
else
    print_error "Django configuration has issues. Please check your settings."
    exit 1
fi

print_success "Backend setup completed successfully!"
print_status "Next steps:"
echo "1. Update your .env file with actual configuration values"
echo "2. Configure your PythonAnywhere web app"
echo "3. Set up your WSGI file"
echo "4. Configure static files mapping"
echo "5. Reload your web app"

print_status "Your backend is ready for deployment!"
