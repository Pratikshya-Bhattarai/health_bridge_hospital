@echo off
echo ========================================
echo   PythonAnywhere Deployment Script
echo ========================================
echo.

echo [1/6] Preparing backend for deployment...
echo.

echo [2/6] Creating production requirements...
copy backend\requirements_production.txt backend\requirements.txt
echo ✅ Production requirements created
echo.

echo [3/6] Creating deployment package...
echo.
echo 📦 Files to upload to PythonAnywhere:
echo    - backend/ (entire folder)
echo    - requirements.txt
echo    - .env (with your Supabase credentials)
echo.

echo [4/6] Environment variables needed:
echo.
echo 🔐 Create .env file with:
echo    SECRET_KEY=your-secret-key-here
echo    DEBUG=False
echo    DB_NAME=your-supabase-db-name
echo    DB_USER=your-supabase-user
echo    DB_PASSWORD=your-supabase-password
echo    DB_HOST=your-supabase-host
echo    DB_PORT=5432
echo.

echo [5/6] PythonAnywhere setup commands:
echo.
echo 🚀 Run these commands in PythonAnywhere Console:
echo.
echo    # Navigate to your project
echo    cd /home/yourusername/health_bridge_hospital/backend
echo.
echo    # Create virtual environment
echo    python3.10 -m venv venv
echo.
echo    # Activate virtual environment
echo    source venv/bin/activate
echo.
echo    # Install requirements
echo    pip install --user -r requirements.txt
echo.
echo    # Run migrations
echo    python manage.py migrate
echo.
echo    # Create superuser
echo    python manage.py createsuperuser
echo.
echo    # Collect static files
echo    python manage.py collectstatic --noinput
echo.

echo [6/6] Web App Configuration:
echo.
echo 🌐 In PythonAnywhere Web tab:
echo    1. Create new web app (Manual Configuration)
echo    2. Python 3.10
echo    3. Source code: /home/yourusername/health_bridge_hospital/backend
echo    4. Working directory: /home/yourusername/health_bridge_hospital/backend
echo    5. WSGI file: /var/www/yourusername_pythonanywhere_com_wsgi.py
echo.

echo ========================================
echo    Deployment Checklist:
echo ========================================
echo.
echo ✅ Backend code prepared
echo ✅ Production settings configured
echo ✅ Requirements file created
echo ✅ Environment variables documented
echo ✅ Deployment commands ready
echo.
echo 📋 Next Steps:
echo    1. Create PythonAnywhere account
echo    2. Upload backend folder
echo    3. Set up virtual environment
echo    4. Configure web app
echo    5. Test API endpoints
echo.
echo 📖 Full guide: PYTHONANYWHERE_DEPLOYMENT_GUIDE.md
echo.
pause
