@echo off
REM Quick PythonAnywhere Deployment Script
REM This script prepares and deploys your backend to PythonAnywhere

echo 🚀 HealthBridge Hospital - Quick PythonAnywhere Deployment
echo =========================================================

REM Check if we're in the right directory
if not exist "backend\manage.py" (
    echo [ERROR] Please run this script from the project root directory
    pause
    exit /b 1
)

echo [INFO] Preparing backend for deployment...

REM Navigate to backend directory
cd backend

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo [INFO] Installing dependencies...
pip install -r requirements.txt

REM Create logs directory
if not exist "logs" mkdir logs

REM Test Django configuration
echo [INFO] Testing Django configuration...
python manage.py check --settings=healthbridge_backend.settings_production

if %errorlevel% neq 0 (
    echo [ERROR] Django configuration has issues. Please check your settings.
    pause
    exit /b 1
)

echo [SUCCESS] Backend is ready for deployment!

REM Go back to project root
cd ..

echo [INFO] Committing changes to Git...
git add .
git commit -m "Fix GitHub workflow and prepare for PythonAnywhere deployment"

echo [INFO] Pushing to GitHub...
git push origin main

echo [SUCCESS] Deployment preparation completed!
echo.
echo [NEXT STEPS]
echo 1. Go to PythonAnywhere and set up your web app
echo 2. Use the WSGI file from: backend/wsgi_pythonanywhere.py
echo 3. Configure static files mapping
echo 4. Reload your web app
echo.
echo [INFO] Your backend will be available at:
echo https://pratikshyabhattarai.pythonanywhere.com
echo.
pause
