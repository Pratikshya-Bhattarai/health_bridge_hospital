# 🆓 HealthBridge Hospital - Free Tier Deployment Guide

## 📋 Overview

This guide is specifically for PythonAnywhere **FREE TIER** users who don't have SSH access. We'll use the web interface and console to deploy your application.

## 🚀 Step-by-Step Deployment

### Step 1: Prepare Your Code

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Note your GitHub repository URL** (you'll need this)

### Step 2: PythonAnywhere Setup

1. **Go to [pythonanywhere.com](https://www.pythonanywhere.com)**
2. **Log in** with your account
3. **Go to "Consoles" tab**
4. **Click "Bash" to start a new console**

### Step 3: Clone Your Repository

In the PythonAnywhere console, run:

```bash
# Clone your repository
git clone https://github.com/yourusername/health_bridge_hospital.git

# Navigate to backend
cd health_bridge_hospital/backend

# Check what we have
ls -la
```

### Step 4: Set Up Virtual Environment

```bash
# Create virtual environment
python3.10 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install --user -r requirements.txt
```

### Step 5: Configure Environment Variables

```bash
# Copy environment template
cp env.example .env

# Edit the environment file
nano .env
```

**Update your .env file with these values:**

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=pratikshyabhattarai.pythonanywhere.com,www.pratikshyabhattarai.pythonanywhere.com

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
EMAIL_HOST_USER=pratikshyabhattarai@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Step 6: Run Initial Setup

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run database migrations
python manage.py migrate --settings=healthbridge_backend.settings_production

# Create superuser
python manage.py createsuperuser --settings=healthbridge_backend.settings_production

# Collect static files
python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
```

### Step 7: Configure Web App

1. **Go to "Web" tab** in PythonAnywhere
2. **Click "Add a new web app"**
3. **Choose "Manual Configuration"**
4. **Choose "Python 3.10"**
5. **Click "Next"**

### Step 8: Configure WSGI File

1. **Click on the WSGI file link** (usually `/var/www/pratikshyabhattarai_pythonanywhere_com_wsgi.py`)
2. **Replace the content** with:

```python
import os
import sys

path = '/home/pratikshyabhattarai/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

activate_this = '/home/pratikshyabhattarai/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

3. **Save the file**

### Step 9: Configure Static Files

1. **Go to "Static files" section**
2. **Add these mappings:**

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/pratikshyabhattarai/health_bridge_hospital/backend/staticfiles` |
| `/media/` | `/home/pratikshyabhattarai/health_bridge_hospital/backend/media` |

### Step 10: Reload Web App

1. **Click "Reload" button** in the Web tab
2. **Visit your site:** `https://pratikshyabhattarai.pythonanywhere.com`

## 🔄 Updating Your App (Manual Process)

Since you don't have SSH access, here's how to update your app:

### Method 1: Using Console

1. **Go to "Consoles" tab**
2. **Start a new Bash console**
3. **Navigate to your project:**
   ```bash
   cd /home/pratikshyabhattarai/health_bridge_hospital
   ```
4. **Pull latest changes:**
   ```bash
   git pull origin main
   ```
5. **Update backend:**
   ```bash
   cd backend
   source venv/bin/activate
   pip install --user -r requirements.txt
   python manage.py migrate --settings=healthbridge_backend.settings_production
   python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
   ```
6. **Reload web app** in the Web tab

### Method 2: Using Files Tab

1. **Go to "Files" tab**
2. **Navigate to your project directory**
3. **Upload new files** as needed
4. **Use console** to run commands

## 🛠️ Troubleshooting

### Common Issues:

1. **Import Errors:**
   - Make sure virtual environment is activated
   - Check all dependencies are installed

2. **Database Connection Issues:**
   - Verify Supabase credentials in .env
   - Test connection in console

3. **Static Files Not Loading:**
   - Run: `python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production`
   - Check static file mappings

4. **Environment Variables Not Loading:**
   - Check .env file exists and has correct values
   - Restart web app after changes

### Useful Console Commands:

```bash
# Check if virtual environment is activated
which python

# Check Django version
python -c "import django; print(django.get_version())"

# Test Django setup
python manage.py check --settings=healthbridge_backend.settings_production

# Check environment variables
python -c "import os; print(os.environ.get('SECRET_KEY'))"
```

## 📊 Your Live URLs

After successful deployment:

- **Your Site:** `https://pratikshyabhattarai.pythonanywhere.com`
- **API:** `https://pratikshyabhattarai.pythonanywhere.com/api/`
- **Admin:** `https://pratikshyabhattarai.pythonanywhere.com/admin/`

## 🎯 Next Steps

1. **Test your API endpoints**
2. **Set up your frontend** to use the production API URL
3. **Consider upgrading** to a paid plan for SSH access and easier deployment

## 💡 Tips for Free Tier

1. **Use console** for all command-line operations
2. **Keep your code on GitHub** for easy updates
3. **Use the Files tab** to browse and edit files
4. **Monitor your CPU seconds** (free tier has limits)
5. **Consider upgrading** if you need more features

## 🎉 Success!

Your HealthBridge Hospital backend is now live on PythonAnywhere free tier!

**Your API is available at:**
`https://pratikshyabhattarai.pythonanywhere.com/api/`

**Update your frontend to use this URL for production!**
