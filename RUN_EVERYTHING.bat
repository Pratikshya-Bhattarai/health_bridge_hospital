@echo off
title HealthBridge Hospital - Complete Setup
color 0A
echo.
echo ========================================
echo 🏥 HealthBridge Hospital - Complete Setup
echo ========================================
echo.
echo This script will set up and run both:
echo - Frontend (Next.js) on http://localhost:3000
echo - Backend (Django) on http://localhost:8000
echo.

REM Set working directory
cd /d "%~dp0"

echo [STEP 1] Checking system requirements...

REM Check Node.js
echo [1/4] Checking Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js not found!
    echo Please install Node.js from: https://nodejs.org/
    echo Choose the LTS version and restart your terminal.
    pause
    exit /b 1
)
echo ✅ Node.js is installed!

REM Check Python
echo [2/4] Checking Python...
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
echo [STEP 2] Setting up Frontend (Next.js)...

REM Install frontend dependencies
if not exist "node_modules" (
    echo Installing frontend dependencies...
    npm install
    if %errorlevel% neq 0 (
        echo ❌ Failed to install frontend dependencies!
        pause
        exit /b 1
    )
    echo ✅ Frontend dependencies installed!
) else (
    echo ✅ Frontend dependencies already installed!
)

echo.
echo [STEP 3] Setting up Backend (Django)...

REM Create virtual environment for backend
if not exist "backend\venv" (
    echo Creating Python virtual environment...
    cd backend
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ❌ Failed to create virtual environment!
        pause
        exit /b 1
    )
    cd ..
    echo ✅ Virtual environment created!
) else (
    echo ✅ Virtual environment already exists!
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
cd backend
call venv\Scripts\activate.bat

REM Install Python dependencies
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
    echo ❌ Failed to install Python dependencies!
    pause
    exit /b 1
)
echo ✅ Python dependencies installed!

REM Setup Django
echo Setting up Django...
if not exist ".env" (
    copy env.example .env
    echo ✅ Environment file created!
)

python setup_django.py
if %errorlevel% neq 0 (
    echo ❌ Django setup failed!
    pause
    exit /b 1
)

echo.
echo [STEP 4] Starting both servers...

echo.
echo ========================================
echo 🚀 STARTING HEALTHBRIDGE HOSPITAL
echo ========================================
echo.
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:8000
echo Admin:    http://localhost:8000/admin/
echo API Docs: http://localhost:8000/api/docs/
echo.
echo Default Login: admin / admin123
echo.
echo Press Ctrl+C to stop both servers
echo.

REM Start both servers in parallel
start "Frontend Server" cmd /k "cd /d %~dp0 && npm run dev"
timeout /t 3 /nobreak >nul
start "Backend Server" cmd /k "cd /d %~dp0\backend && call venv\Scripts\activate.bat && python manage.py runserver"

echo.
echo ✅ Both servers are starting!
echo.
echo Frontend will open at: http://localhost:3000
echo Backend API will be at: http://localhost:8000
echo.
echo You can now:
echo 1. Visit the website at http://localhost:3000
echo 2. Test the API at http://localhost:8000/api/docs/
echo 3. Access admin panel at http://localhost:8000/admin/
echo.
echo Press any key to exit...
pause >nul
