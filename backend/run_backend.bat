@echo off
title HealthBridge Hospital - Django Backend
color 0A
echo.
echo ========================================
echo 🏥 HealthBridge Hospital - Django Backend
echo ========================================
echo.

REM Set working directory
cd /d "%~dp0"

echo [STEP 1] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found!
    echo Please install Python from: https://python.org/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)
echo ✅ Python is installed!

echo.
echo [STEP 2] Setting up virtual environment...
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ❌ Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created!
) else (
    echo ✅ Virtual environment already exists!
)

echo.
echo [STEP 3] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [STEP 4] Installing dependencies...
if not exist "requirements.txt" (
    echo Creating requirements.txt...
    echo Django==4.2.7 > requirements.txt
    echo djangorestframework==3.14.0 >> requirements.txt
    echo django-cors-headers==4.3.1 >> requirements.txt
    echo supabase==2.0.2 >> requirements.txt
    echo python-dotenv==1.0.0 >> requirements.txt
    echo django-filter==23.3 >> requirements.txt
    echo drf-spectacular==0.26.5 >> requirements.txt
    echo psycopg2-binary==2.9.7 >> requirements.txt
    echo celery==5.3.4 >> requirements.txt
    echo redis==5.0.1 >> requirements.txt
    echo django-environ==0.11.2 >> requirements.txt
    echo Pillow==10.1.0 >> requirements.txt
    echo gunicorn==21.2.0 >> requirements.txt
    echo whitenoise==6.6.0 >> requirements.txt
    echo djangorestframework-simplejwt==5.3.0 >> requirements.txt
    echo django-extensions==3.2.3 >> requirements.txt
    echo python-decouple==3.8 >> requirements.txt
    echo requests==2.31.0 >> requirements.txt
)

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies!
    pause
    exit /b 1
)
echo ✅ Dependencies installed!

echo.
echo [STEP 5] Setting up environment...
if not exist ".env" (
    echo Creating environment file...
    copy env.example .env
    echo ✅ Environment file created!
) else (
    echo ✅ Environment file already exists!
)

echo.
echo [STEP 6] Setting up Django...
python setup_django.py
if %errorlevel% neq 0 (
    echo ❌ Django setup failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo 🚀 STARTING DJANGO BACKEND SERVER
echo ========================================
echo.
echo Backend API: http://localhost:8000
echo Admin Panel: http://localhost:8000/admin/
echo API Docs:    http://localhost:8000/api/docs/
echo.
echo Default Login: admin / admin123
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver
