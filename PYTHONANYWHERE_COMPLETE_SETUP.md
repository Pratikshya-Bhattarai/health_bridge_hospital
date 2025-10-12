# 🏥 HealthBridge Hospital - Complete PythonAnywhere Setup Guide

## 🚨 GitHub Issues Fixed

The GitHub workflow has been updated to fix the following issues:
- ✅ Fixed path inconsistencies in deploy.yml
- ✅ Added proper error handling
- ✅ Added manual workflow trigger
- ✅ Improved deployment script with better logging

## 🚀 Complete PythonAnywhere Setup

### Prerequisites
- PythonAnywhere account (free tier is fine)
- GitHub repository with your code
- Supabase database (or any PostgreSQL database)

### Step 1: Prepare Your Local Environment

1. **Run the setup script locally:**
   ```bash
   # Windows
   cd backend
   scripts\setup-pythonanywhere-complete.bat
   
   # Linux/Mac
   cd backend
   chmod +x scripts/setup-pythonanywhere-complete.sh
   ./scripts/setup-pythonanywhere-complete.sh
   ```

2. **Update your .env file with real values:**
   ```env
   SECRET_KEY=your-actual-secret-key
   DEBUG=False
   ALLOWED_HOSTS=pratikshyabhattarai.pythonanywhere.com,www.pratikshyabhattarai.pythonanywhere.com
   
   # Database Configuration (Supabase)
   DB_NAME=your-actual-db-name
   DB_USER=your-actual-db-user
   DB_PASSWORD=your-actual-db-password
   DB_HOST=db.your-project.supabase.co
   DB_PORT=5432
   
   # Supabase Configuration
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-actual-supabase-key
   SUPABASE_SERVICE_ROLE_KEY=your-actual-service-role-key
   
   # JWT Settings
   JWT_SECRET_KEY=your-actual-jwt-secret
   JWT_ALGORITHM=HS256
   JWT_ACCESS_TOKEN_LIFETIME=60
   JWT_REFRESH_TOKEN_LIFETIME=1440
   
   # Email Configuration
   EMAIL_HOST_USER=pratikshyabhattarai@gmail.com
   EMAIL_HOST_PASSWORD=your-actual-app-password
   ```

3. **Test locally:**
   ```bash
   python manage.py check --settings=healthbridge_backend.settings_production
   python manage.py runserver --settings=healthbridge_backend.settings_production
   ```

### Step 2: Push to GitHub

```bash
git add .
git commit -m "Fix GitHub workflow and prepare for PythonAnywhere deployment"
git push origin main
```

### Step 3: PythonAnywhere Setup

#### Option A: Using SSH (Paid Plans)

If you have SSH access, the GitHub workflow will automatically deploy:

1. **Set up GitHub Secrets:**
   - Go to your GitHub repository
   - Settings → Secrets and variables → Actions
   - Add these secrets:
     - `PYTHONANYWHERE_HOST`: your PythonAnywhere SSH host
     - `PYTHONANYWHERE_USERNAME`: your PythonAnywhere username
     - `PYTHONANYWHERE_SSH_KEY`: your SSH private key

2. **The workflow will automatically:**
   - Pull latest code
   - Install dependencies
   - Run migrations
   - Collect static files
   - Reload the application

#### Option B: Manual Setup (Free Tier)

1. **Go to PythonAnywhere Console:**
   - Log in to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Go to "Consoles" tab
   - Start a new Bash console

2. **Clone your repository:**
   ```bash
   git clone https://github.com/yourusername/health_bridge_hospital.git
   cd health_bridge_hospital/backend
   ```

3. **Set up virtual environment:**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --user -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp env.example .env
   nano .env  # Edit with your actual values
   ```

5. **Run setup:**
   ```bash
   python manage.py migrate --settings=healthbridge_backend.settings_production
   python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
   python manage.py createsuperuser --settings=healthbridge_backend.settings_production
   ```

### Step 4: Configure Web App

1. **Go to "Web" tab in PythonAnywhere**
2. **Click "Add a new web app"**
3. **Choose "Manual Configuration"**
4. **Choose "Python 3.10"**
5. **Click "Next"**

### Step 5: Configure WSGI File

1. **Click on the WSGI file link** (usually `/var/www/pratikshyabhattarai_pythonanywhere_com_wsgi.py`)
2. **Replace the content with:**

```python
import os
import sys

# Add the project directory to Python path
path = '/home/pratikshyabhattarai/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

# Activate virtual environment
activate_this = '/home/pratikshyabhattarai/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

3. **Save the file**

### Step 6: Configure Static Files

1. **Go to "Static files" section**
2. **Add these mappings:**

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/pratikshyabhattarai/health_bridge_hospital/backend/staticfiles` |
| `/media/` | `/home/pratikshyabhattarai/health_bridge_hospital/backend/media` |

### Step 7: Reload Web App

1. **Click "Reload" button** in the Web tab
2. **Visit your site:** `https://pratikshyabhattarai.pythonanywhere.com`

## 🔄 Updating Your App

### With SSH (Paid Plans)
- Push to GitHub, and the workflow will automatically deploy

### Without SSH (Free Tier)
1. **Go to Console**
2. **Navigate to project:**
   ```bash
   cd /home/pratikshyabhattarai/health_bridge_hospital
   ```
3. **Pull latest changes:**
   ```bash
   git pull origin main
   ```
4. **Update backend:**
   ```bash
   cd backend
   source venv/bin/activate
   pip install --user -r requirements.txt
   python manage.py migrate --settings=healthbridge_backend.settings_production
   python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
   ```
5. **Reload web app** in the Web tab

## 🛠️ Troubleshooting

### Common Issues:

1. **Import Errors:**
   - Check virtual environment is activated
   - Verify all dependencies are installed
   - Check Python path in WSGI file

2. **Database Connection Issues:**
   - Verify database credentials in .env
   - Test connection in console
   - Check Supabase connection

3. **Static Files Not Loading:**
   - Run: `python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production`
   - Check static file mappings in Web tab
   - Verify static files directory exists

4. **Environment Variables Not Loading:**
   - Check .env file exists and has correct values
   - Restart web app after changes
   - Verify dotenv is installed

### Useful Commands:

```bash
# Check Django setup
python manage.py check --settings=healthbridge_backend.settings_production

# Test database connection
python manage.py dbshell --settings=healthbridge_backend.settings_production

# Check environment variables
python -c "import os; print(os.environ.get('SECRET_KEY'))"

# View logs
tail -f logs/django.log
```

## 📊 Your Live URLs

After successful deployment:

- **Your Site:** `https://pratikshyabhattarai.pythonanywhere.com`
- **API:** `https://pratikshyabhattarai.pythonanywhere.com/api/`
- **Admin:** `https://pratikshyabhattarai.pythonanywhere.com/admin/`

## 🎯 Next Steps

1. **Test your API endpoints**
2. **Update your frontend** to use the production API URL
3. **Set up monitoring** and logging
4. **Consider upgrading** to a paid plan for easier deployment

## 🎉 Success!

Your HealthBridge Hospital backend is now live on PythonAnywhere!

**Your API is available at:**
`https://pratikshyabhattarai.pythonanywhere.com/api/`

**Update your frontend to use this URL for production!**
