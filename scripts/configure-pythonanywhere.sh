#!/bin/bash

# HealthBridge Hospital - PythonAnywhere Configuration Script
# This script configures the PythonAnywhere web app for GitHub integration

set -e

echo "🔧 Configuring PythonAnywhere for HealthBridge Hospital..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# Get username
if [ -z "$PYTHONANYWHERE_USERNAME" ]; then
    read -p "Enter your PythonAnywhere username: " PYTHONANYWHERE_USERNAME
fi

print_status "Configuring for user: $PYTHONANYWHERE_USERNAME"

# Create WSGI configuration file
print_status "Creating WSGI configuration file..."

cat > /var/www/${PYTHONANYWHERE_USERNAME}_pythonanywhere_com_wsgi.py << EOF
import os
import sys

# Add your project directory to the Python path
path = '/home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

# Activate virtual environment
activate_this = '/home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
EOF

print_status "WSGI file created at: /var/www/${PYTHONANYWHERE_USERNAME}_pythonanywhere_com_wsgi.py"

# Create static files directory
print_status "Creating static files directory..."
mkdir -p /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/staticfiles
mkdir -p /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/media

# Set up environment variables
print_status "Setting up environment variables..."

# Create .env file if it doesn't exist
if [ ! -f "/home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/.env" ]; then
    print_warning "Creating .env file from template..."
    cp /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/env.example /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/.env
    print_warning "Please update .env file with your actual credentials!"
fi

# Set up SSH key for GitHub access
print_status "Setting up SSH key for GitHub access..."

# Create .ssh directory if it doesn't exist
mkdir -p /home/${PYTHONANYWHERE_USERNAME}/.ssh
chmod 700 /home/${PYTHONANYWHERE_USERNAME}/.ssh

# Generate SSH key if it doesn't exist
if [ ! -f "/home/${PYTHONANYWHERE_USERNAME}/.ssh/id_rsa" ]; then
    print_status "Generating SSH key for GitHub access..."
    ssh-keygen -t rsa -b 4096 -C "${PYTHONANYWHERE_USERNAME}@pythonanywhere.com" -f /home/${PYTHONANYWHERE_USERNAME}/.ssh/id_rsa -N ""
    chmod 600 /home/${PYTHONANYWHERE_USERNAME}/.ssh/id_rsa
    chmod 644 /home/${PYTHONANYWHERE_USERNAME}/.ssh/id_rsa.pub
fi

print_info "SSH Public Key (add this to GitHub):"
cat /home/${PYTHONANYWHERE_USERNAME}/.ssh/id_rsa.pub

# Set up Git configuration
print_status "Setting up Git configuration..."
cd /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital
git config --global user.name "${PYTHONANYWHERE_USERNAME}"
git config --global user.email "${PYTHONANYWHERE_USERNAME}@pythonanywhere.com"

# Set up SSH for Git
print_status "Setting up SSH for Git..."
if [ ! -f "/home/${PYTHONANYWHERE_USERNAME}/.ssh/config" ]; then
    cat > /home/${PYTHONANYWHERE_USERNAME}/.ssh/config << EOF
Host github.com
    HostName github.com
    User git
    IdentityFile /home/${PYTHONANYWHERE_USERNAME}/.ssh/id_rsa
    StrictHostKeyChecking no
EOF
    chmod 600 /home/${PYTHONANYWHERE_USERNAME}/.ssh/config
fi

# Test SSH connection to GitHub
print_status "Testing SSH connection to GitHub..."
ssh -T git@github.com || print_warning "SSH connection test failed. Please add your SSH key to GitHub."

# Set up webhook for automatic deployment
print_status "Setting up webhook for automatic deployment..."

# Create webhook script
cat > /home/${PYTHONANYWHERE_USERNAME}/webhook_deploy.sh << 'EOF'
#!/bin/bash
cd /home/bepratikshya/health_bridge_hospital
git pull origin main
cd backend
source venv/bin/activate
pip install --user -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
touch /var/www/bepratikshya_pythonanywhere_com_wsgi.py
echo "Deployment completed at $(date)"
EOF

chmod +x /home/${PYTHONANYWHERE_USERNAME}/webhook_deploy.sh

print_status "Webhook script created at: /home/${PYTHONANYWHERE_USERNAME}/webhook_deploy.sh"

# Create deployment script
print_status "Creating deployment script..."

cat > /home/${PYTHONANYWHERE_USERNAME}/deploy.sh << 'EOF'
#!/bin/bash
echo "🚀 Deploying HealthBridge Hospital..."

# Navigate to project directory
cd /home/bepratikshya/health_bridge_hospital

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
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create logs directory
mkdir -p logs

# Restart web app
echo "🔄 Restarting web app..."
touch /var/www/bepratikshya_pythonanywhere_com_wsgi.py

echo "✅ Deployment completed successfully!"
echo "🌐 Your app is available at: https://bepratikshya.pythonanywhere.com"
EOF

chmod +x /home/${PYTHONANYWHERE_USERNAME}/deploy.sh

print_status "Deployment script created at: /home/${PYTHONANYWHERE_USERNAME}/deploy.sh"

# Set up cron job for automatic updates (optional)
print_status "Setting up cron job for automatic updates..."

# Add cron job to check for updates every hour
(crontab -l 2>/dev/null; echo "0 * * * * /home/${PYTHONANYWHERE_USERNAME}/deploy.sh >> /home/${PYTHONANYWHERE_USERNAME}/deploy.log 2>&1") | crontab -

print_status "Cron job added for automatic updates"

# Final instructions
print_status "✅ PythonAnywhere configuration completed!"
echo ""
print_info "📋 Next steps:"
echo "1. Add your SSH public key to GitHub:"
echo "   - Go to GitHub → Settings → SSH and GPG keys"
echo "   - Add the key shown above"
echo ""
echo "2. Update your .env file with actual credentials:"
echo "   - Edit: /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/.env"
echo ""
echo "3. Configure static files in PythonAnywhere Web tab:"
echo "   - URL: /static/"
echo "   - Directory: /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/staticfiles"
echo "   - URL: /media/"
echo "   - Directory: /home/${PYTHONANYWHERE_USERNAME}/health_bridge_hospital/backend/media"
echo ""
echo "4. Reload your web app in PythonAnywhere Web tab"
echo ""
echo "5. Test your deployment:"
echo "   - https://${PYTHONANYWHERE_USERNAME}.pythonanywhere.com"
echo "   - https://${PYTHONANYWHERE_USERNAME}.pythonanywhere.com/api/"
echo ""
print_info "🔧 Manual deployment command:"
echo "   /home/${PYTHONANYWHERE_USERNAME}/deploy.sh"
echo ""
print_info "📊 Monitor deployment logs:"
echo "   tail -f /home/${PYTHONANYWHERE_USERNAME}/deploy.log"
echo ""
print_status "🎉 HealthBridge Hospital is ready for automated deployment!"
