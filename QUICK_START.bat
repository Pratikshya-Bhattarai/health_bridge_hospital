@echo off
title HealthBridge Hospital - Quick Start
color 0A
echo.
echo ========================================
echo 🏥 HealthBridge Hospital - Quick Start
echo ========================================
echo.

REM Set working directory
cd /d "%~dp0"

echo [STEP 1] Starting Frontend (Next.js)...
if not exist "node_modules" (
    echo Installing dependencies...
    npm install
)
start "Frontend" cmd /k "npm run dev"

echo.
echo [STEP 2] Starting Backend (Django)...
cd backend
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate.bat
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
if not exist ".env" (
    copy env.example .env
)
python setup_django.py
start "Backend" cmd /k "python manage.py runserver"

echo.
echo ✅ Both servers are starting!
echo.
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:8000
echo.
echo Press any key to exit...
pause >nul