@echo off
REM HealthBridge Hospital - Complete PythonAnywhere Setup Script for Windows
REM This script prepares the backend for PythonAnywhere deployment

echo 🚀 Starting HealthBridge Hospital Backend Setup for PythonAnywhere...

REM Check if we're in the right directory
if not exist "manage.py" (
    echo [ERROR] Please run this script from the backend directory
    pause
    exit /b 1
)

echo [INFO] Setting up HealthBridge Hospital Backend...

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
    echo [SUCCESS] Virtual environment created
) else (
    echo [INFO] Virtual environment already exists
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo [INFO] Installing Python dependencies...
pip install -r requirements.txt

REM Create logs directory
echo [INFO] Creating logs directory...
if not exist "logs" mkdir logs

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo [INFO] Creating .env file from template...
    copy env.example .env
    echo [WARNING] Please update .env file with your actual configuration values
) else (
    echo [INFO] .env file already exists
)

REM Test Django setup
echo [INFO] Testing Django configuration...
python manage.py check --settings=healthbridge_backend.settings_production

if %errorlevel% equ 0 (
    echo [SUCCESS] Django configuration is valid
) else (
    echo [ERROR] Django configuration has issues. Please check your settings.
    pause
    exit /b 1
)

echo [SUCCESS] Backend setup completed successfully!
echo [INFO] Next steps:
echo 1. Update your .env file with actual configuration values
echo 2. Push your code to GitHub
echo 3. Configure your PythonAnywhere web app
echo 4. Set up your WSGI file
echo 5. Configure static files mapping
echo 6. Reload your web app

echo [INFO] Your backend is ready for deployment!
pause
