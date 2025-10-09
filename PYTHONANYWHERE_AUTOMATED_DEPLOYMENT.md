# 🚀 Automated PythonAnywhere Deployment Guide

## 📋 Overview

This guide sets up automated deployment to PythonAnywhere using GitHub Actions and proper environment variable handling.

## 🔐 Prerequisites

1. **PythonAnywhere Account** (Free tier available)
   - Username: `bepratikshya` (your account)
   - Password: `rxcqm%pD995B6p+`

2. **GitHub Repository** with your code
3. **Supabase Project** with database credentials
4. **SSH Key** for PythonAnywhere access

## 🛠️ Setup Steps

### 1. Configure GitHub Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions, and add:

```
PYTHONANYWHERE_HOST: pythonanywhere.com
PYTHONANYWHERE_USERNAME: bepratikshya
PYTHONANYWHERE_SSH_KEY: [Your SSH private key]
```

### 2. Set Up SSH Key for PythonAnywhere

#### Option A: Generate New SSH Key (Recommended)

```bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f ~/.ssh/pythonanywhere_key

# Copy public key to PythonAnywhere
cat ~/.ssh/pythonanywhere_key.pub
```

#### Option B: Use Existing SSH Key

If you already have an SSH key, use that instead.

### 3. Configure PythonAnywhere SSH Access

1. **Log in to PythonAnywhere** with your credentials
2. **Go to Account tab** → SSH keys
3. **Add your public SSH key**
4. **Enable SSH access** (if not already enabled)

### 4. Set Up Environment Variables

#### On PythonAnywhere:

1. **Navigate to your project directory:**
   ```bash
   cd /home/bepratikshya/health_bridge_hospital/backend
   ```

2. **Create .env file:**
   ```bash
   nano .env
   ```

3. **Add your environment variables:**
   ```env
   # Django Settings
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=bepratikshya.pythonanywhere.com,www.bepratikshya.pythonanywhere.com
   
   # Database Configuration (Supabase)
   DB_NAME=your-supabase-db-name
   DB_USER=your-supabase-user
   DB_PASSWORD=your-supabase-password
   DB_HOST=db.your-project.supabase.co
   DB_PORT=5432
   
   # Supabase Configuration
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-supabase-anon-key
   SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
   
   # JWT Settings
   JWT_SECRET_KEY=your-jwt-secret-key
   JWT_ALGORITHM=HS256
   JWT_ACCESS_TOKEN_LIFETIME=60
   JWT_REFRESH_TOKEN_LIFETIME=1440
   
   # Email Configuration
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   
   # CORS Settings
   CORS_ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app,http://localhost:3000
   ```

### 5. Initial PythonAnywhere Setup

#### A. Clone Repository on PythonAnywhere

```bash
# SSH into PythonAnywhere
ssh bepratikshya@pythonanywhere.com

# Clone your repository
git clone https://github.com/yourusername/health_bridge_hospital.git
cd health_bridge_hospital/backend
```

#### B. Set Up Virtual Environment

```bash
# Create virtual environment
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install --user -r requirements.txt
```

#### C. Configure Web App

1. **Go to Web tab** in PythonAnywhere dashboard
2. **Click "Add a new web app"**
3. **Choose "Manual Configuration"**
4. **Select Python 3.10**

#### D. Configure WSGI File

**File:** `/var/www/bepratikshya_pythonanywhere_com_wsgi.py`

```python
import os
import sys

# Add your project directory to the Python path
path = '/home/bepratikshya/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

# Activate virtual environment
activate_this = '/home/bepratikshya/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### E. Configure Static Files

In PythonAnywhere Web tab → Static files:

- **URL:** `/static/`
- **Directory:** `/home/bepratikshya/health_bridge_hospital/backend/staticfiles`

- **URL:** `/media/`
- **Directory:** `/home/bepratikshya/health_bridge_hospital/backend/media`

### 6. Test Initial Deployment

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Create logs directory
mkdir -p logs
```

### 7. Reload Web App

1. **Go to Web tab** in PythonAnywhere
2. **Click the green "Reload" button**
3. **Test your deployment:** `https://bepratikshya.pythonanywhere.com`

## 🔄 Automated Deployment

### How It Works

1. **Push to GitHub:** When you push code to the `main` branch
2. **GitHub Actions:** Automatically triggers the deployment workflow
3. **SSH Connection:** Connects to PythonAnywhere via SSH
4. **Code Update:** Pulls latest changes from GitHub
5. **Dependencies:** Updates Python packages
6. **Database:** Runs migrations
7. **Static Files:** Collects static files
8. **Restart:** Restarts the web application

### Manual Deployment

If you need to deploy manually:

```bash
# SSH into PythonAnywhere
ssh bepratikshya@pythonanywhere.com

# Navigate to project
cd /home/bepratikshya/health_bridge_hospital

# Pull latest changes
git pull origin main

# Navigate to backend
cd backend

# Activate virtual environment
source venv/bin/activate

# Update dependencies
pip install --user -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart web app (touch WSGI file)
touch /var/www/bepratikshya_pythonanywhere_com_wsgi.py
```

## 🔧 Troubleshooting

### Common Issues:

1. **SSH Connection Failed:**
   - Check SSH key is correctly added to GitHub secrets
   - Verify SSH key is added to PythonAnywhere account
   - Test SSH connection manually: `ssh bepratikshya@pythonanywhere.com`

2. **Environment Variables Not Loading:**
   - Check .env file exists in backend directory
   - Verify all required variables are set
   - Check file permissions: `chmod 600 .env`

3. **Database Connection Issues:**
   - Verify Supabase credentials in .env file
   - Check database host and port
   - Test connection from PythonAnywhere console

4. **Static Files Not Loading:**
   - Run `python manage.py collectstatic --noinput`
   - Check static file mappings in PythonAnywhere Web tab
   - Verify STATIC_ROOT setting

5. **Import Errors:**
   - Check virtual environment is activated
   - Verify all packages are installed: `pip list`
   - Check Python path in WSGI file

### Useful Commands:

```bash
# Check logs
tail -f /var/log/bepratikshya.pythonanywhere.com.error.log

# Check Django logs
tail -f /home/bepratikshya/health_bridge_hospital/backend/logs/django.log

# Test Django setup
python manage.py check --deploy

# Check environment variables
python manage.py shell -c "import os; print(os.environ.get('SECRET_KEY'))"
```

## 📊 Monitoring

### Health Checks:

1. **API Endpoints:**
   - `https://bepratikshya.pythonanywhere.com/api/`
   - `https://bepratikshya.pythonanywhere.com/api/appointments/`
   - `https://bepratikshya.pythonanywhere.com/api/doctors/`

2. **Database Connection:**
   - Check Django admin: `https://bepratikshya.pythonanywhere.com/admin/`
   - Test API endpoints with database queries

3. **Static Files:**
   - Check CSS/JS loading in browser
   - Verify static file URLs

## 🚀 Production Optimizations

1. **Enable HTTPS:** PythonAnywhere provides SSL certificates
2. **Set up monitoring:** Use PythonAnywhere's built-in monitoring
3. **Configure backups:** Set up database backups
4. **Performance tuning:** Optimize Django settings for production

## 📞 Support

- **PythonAnywhere Help:** [help.pythonanywhere.com](https://help.pythonanywhere.com)
- **GitHub Actions:** [docs.github.com/actions](https://docs.github.com/en/actions)
- **Django Deployment:** [docs.djangoproject.com](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

## 🎉 Success!

Your HealthBridge Hospital backend is now set up for automated deployment to PythonAnywhere!

**Your API will be available at:**
`https://bepratikshya.pythonanywhere.com/api/`

**Next steps:**
1. Test all API endpoints
2. Update frontend to use production API
3. Set up monitoring and alerts
4. Configure custom domain (optional)
