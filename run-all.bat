@echo off
echo ========================================
echo HealthBridge Hospital - Complete Setup
echo ========================================
echo.

echo Starting complete setup for HealthBridge Hospital...
echo This will set up both Frontend (Next.js) and Backend (Django)
echo.

REM Check if Node.js is installed
echo [1/6] Checking Node.js installation...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed!
    echo.
    echo Please install Node.js from: https://nodejs.org/
    echo Choose the LTS version and restart your terminal.
    echo.
    pause
    exit /b 1
)
echo ✓ Node.js is installed!

REM Check if Python is installed
echo [2/6] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python from: https://python.org/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)
echo ✓ Python is installed!

REM Setup Frontend
echo [3/6] Setting up Frontend (Next.js)...
cd /d "%~dp0"
if not exist "node_modules" (
    echo Installing frontend dependencies...
    npm install
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install frontend dependencies!
        pause
        exit /b 1
    )
    echo ✓ Frontend dependencies installed!
) else (
    echo ✓ Frontend dependencies already installed!
)

REM Setup Backend
echo [4/6] Setting up Backend (Django)...
if not exist "backend" (
    echo Creating backend directory...
    mkdir backend
)
cd backend

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo ✓ Virtual environment created!
) else (
    echo ✓ Virtual environment already exists!
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
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
)

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install backend dependencies!
    pause
    exit /b 1
)
echo ✓ Backend dependencies installed!

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating environment configuration...
    copy env.example .env
    echo ✓ Environment file created!
) else (
    echo ✓ Environment file already exists!
)

cd ..

echo [5/6] Starting services...
echo.

REM Start backend in background
echo Starting Django backend server...
cd backend
start "Django Backend" cmd /k "call venv\Scripts\activate.bat && python manage.py runserver 8000"
cd ..

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend
echo Starting Next.js frontend server...
start "Next.js Frontend" cmd /k "npm run dev"

echo [6/6] Setup Complete!
echo.
echo ========================================
echo Services Started Successfully!
echo ========================================
echo.
echo Frontend (Next.js): http://localhost:3000
echo Backend (Django):   http://localhost:8000
echo API Documentation:  http://localhost:8000/api/docs/
echo.
echo Both servers are now running in separate windows.
echo Close those windows to stop the servers.
echo.
echo Press any key to exit this setup script...
pause >nul
