# 🚀 PythonAnywhere Deployment Guide for HealthBridge Backend

## 📋 Prerequisites

1. **PythonAnywhere Account** (Free tier available)
2. **Supabase Project** (Already configured)
3. **GitHub Repository** (Optional but recommended)

## 🎯 Step-by-Step Deployment

### 1. Create PythonAnywhere Account

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Click "Create a Beginner account" (Free tier)
3. Verify your email address
4. Complete the registration

### 2. Prepare Your Backend for Deployment

#### A. Create Production Requirements File

```bash
# In your backend directory
pip freeze > requirements.txt
```

#### B. Update Django Settings for Production

Create `backend/healthbridge_backend/settings_production.py`:

```python
import os
from .settings import *

# Production settings
DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'www.yourusername.pythonanywhere.com']

# Database configuration (Supabase)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'your_supabase_db_name'),
        'USER': os.environ.get('DB_USER', 'your_supabase_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'your_supabase_password'),
        'HOST': os.environ.get('DB_HOST', 'your_supabase_host'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# CORS settings for frontend
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.vercel.app",
    "http://localhost:3001",
    "http://localhost:3000",
]

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/yourusername/healthbridge_backend/logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

### 3. Upload Your Code to PythonAnywhere

#### Option A: Using Git (Recommended)

1. **Push your code to GitHub:**
```bash
git add .
git commit -m "Prepare for PythonAnywhere deployment"
git push origin main
```

2. **In PythonAnywhere Console:**
```bash
git clone https://github.com/yourusername/health_bridge_hospital.git
cd health_bridge_hospital/backend
```

#### Option B: Direct Upload

1. **Create a ZIP file** of your backend folder
2. **Upload via PythonAnywhere Files tab**
3. **Extract the files**

### 4. Set Up Virtual Environment

In PythonAnywhere Console:

```bash
# Navigate to your project
cd /home/yourusername/health_bridge_hospital/backend

# Create virtual environment
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install --user -r requirements.txt
```

### 5. Configure Environment Variables

Create `.env` file in your backend directory:

```bash
# In PythonAnywhere Console
nano .env
```

Add your environment variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
DB_NAME=your-supabase-db-name
DB_USER=your-supabase-user
DB_PASSWORD=your-supabase-password
DB_HOST=your-supabase-host
DB_PORT=5432
```

### 6. Run Django Migrations

```bash
# Activate virtual environment
source venv/bin/activate

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 7. Configure Web App

1. **Go to Web tab** in PythonAnywhere dashboard
2. **Click "Add a new web app"**
3. **Choose "Manual Configuration"**
4. **Select Python 3.10**
5. **Configure the following:**

#### WSGI Configuration File:

```python
# /var/www/yourusername_pythonanywhere_com_wsgi.py

import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

# Activate virtual environment
activate_this = '/home/yourusername/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 8. Configure Static Files

1. **Go to Web tab**
2. **Click "Static files"**
3. **Add static file mapping:**
   - **URL:** `/static/`
   - **Directory:** `/home/yourusername/health_bridge_hospital/backend/staticfiles`

### 9. Test Your Deployment

1. **Reload your web app** (click the green reload button)
2. **Visit your domain:** `https://yourusername.pythonanywhere.com`
3. **Test API endpoints:**
   - `https://yourusername.pythonanywhere.com/api/appointments/`
   - `https://yourusername.pythonanywhere.com/api/doctors/`

### 10. Update Frontend API URLs

Update your frontend to use the PythonAnywhere backend:

```typescript
// lib/api.ts
const API_BASE_URL = 'https://yourusername.pythonanywhere.com/api'
```

## 🔧 Troubleshooting

### Common Issues:

1. **Import Errors:**
   - Check virtual environment is activated
   - Verify all packages are installed

2. **Database Connection Issues:**
   - Verify Supabase credentials
   - Check network connectivity

3. **Static Files Not Loading:**
   - Run `python manage.py collectstatic`
   - Check static file mappings

4. **CORS Issues:**
   - Update CORS_ALLOWED_ORIGINS in settings
   - Install django-cors-headers

### Useful Commands:

```bash
# Check logs
tail -f /var/log/yourusername.pythonanywhere.com.error.log

# Check Django logs
tail -f /home/yourusername/health_bridge_hospital/backend/logs/django.log

# Restart web app
# Go to Web tab and click "Reload"
```

## 📊 Monitoring

1. **Check web app status** in PythonAnywhere dashboard
2. **Monitor logs** for errors
3. **Test API endpoints** regularly
4. **Check database connectivity**

## 🚀 Production Optimizations

1. **Enable HTTPS** (PythonAnywhere provides SSL)
2. **Set up monitoring** and logging
3. **Configure backups** for your database
4. **Set up error tracking** (Sentry, etc.)

## 📞 Support

- **PythonAnywhere Help:** [help.pythonanywhere.com](https://help.pythonanywhere.com)
- **Django Deployment:** [docs.djangoproject.com](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

## 🎉 Your Backend is Now Live!

**Your Django API will be available at:**
`https://yourusername.pythonanywhere.com/api/`

**Update your frontend to use this URL for production!**
