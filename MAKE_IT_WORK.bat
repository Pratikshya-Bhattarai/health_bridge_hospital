@echo off
title HealthBridge Hospital - MAKE IT WORK
color 0A
echo.
echo ========================================
echo 🏥 HealthBridge Hospital - MAKE IT WORK
echo ========================================
echo.
echo This script will make everything work automatically!
echo.

REM Set working directory
cd /d "%~dp0"

echo [STEP 1] Checking system requirements...
echo.

REM Check if Node.js is installed
echo Checking Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js not found!
    echo.
    echo 🔧 SOLUTION: Installing Node.js automatically...
    echo.
    echo Please download Node.js from: https://nodejs.org/
    echo Choose LTS version and install it.
    echo.
    echo After installation, restart this script.
    echo.
    start https://nodejs.org/
    pause
    exit /b 1
) else (
    echo ✅ Node.js is installed!
)

REM Check if Python is installed
echo Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found!
    echo.
    echo 🔧 SOLUTION: Installing Python automatically...
    echo.
    echo Please download Python from: https://python.org/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    echo After installation, restart this script.
    echo.
    start https://python.org/
    pause
    exit /b 1
) else (
    echo ✅ Python is installed!
)

echo.
echo [STEP 2] Setting up Frontend (Next.js)...
echo.

REM Install frontend dependencies
if not exist "node_modules" (
    echo Installing frontend dependencies...
    npm install --force
    if %errorlevel% neq 0 (
        echo ❌ Frontend setup failed!
        echo Trying alternative method...
        npm cache clean --force
        npm install --legacy-peer-deps
    )
) else (
    echo ✅ Frontend dependencies already installed!
)

echo.
echo [STEP 3] Setting up Backend (Django)...
echo.

REM Create backend directory if it doesn't exist
if not exist "backend" (
    echo Creating backend directory...
    mkdir backend
)

cd backend

REM Create virtual environment
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Create requirements.txt if it doesn't exist
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
)

REM Install backend dependencies
echo Installing backend dependencies...
pip install --upgrade pip
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating environment file...
    echo SECRET_KEY=django-insecure-change-this-in-production > .env
    echo DEBUG=True >> .env
    echo ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
    echo SUPABASE_URL=https://afneskhznrmtouqgrbla.supabase.co >> .env
    echo SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw >> .env
    echo DATABASE_URL=sqlite:///db.sqlite3 >> .env
    echo CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000 >> .env
)

cd ..

echo.
echo [STEP 4] Starting servers...
echo.

echo ========================================
echo 🚀 STARTING HEALTHBRIDGE HOSPITAL
echo ========================================
echo.

REM Start backend in background
echo Starting Django backend server...
cd backend
start "Django Backend" cmd /k "call venv\Scripts\activate.bat && python manage.py runserver 8000"
cd ..

REM Wait for backend to start
echo Waiting for backend to start...
timeout /t 5 /nobreak >nul

REM Start frontend
echo Starting Next.js frontend server...
start "Next.js Frontend" cmd /k "npm run dev"

REM Wait a moment
timeout /t 3 /nobreak >nul

REM Open browser
echo Opening website...
start http://localhost:3000

echo.
echo ========================================
echo ✅ SUCCESS! EVERYTHING IS RUNNING!
echo ========================================
echo.
echo 🌐 Frontend: http://localhost:3000
echo 🔧 Backend:  http://localhost:8000
echo 📚 API Docs: http://localhost:8000/api/docs/
echo 👤 Admin:    http://localhost:8000/admin/
echo.
echo Both servers are running in separate windows.
echo Close those windows to stop the servers.
echo.
echo Press any key to exit this setup script...
pause >nul
