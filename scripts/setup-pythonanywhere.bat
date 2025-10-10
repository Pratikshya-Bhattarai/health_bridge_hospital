@echo off
REM HealthBridge Hospital - PythonAnywhere Initial Setup Script for Windows
REM This script sets up the initial deployment environment on PythonAnywhere

echo 🏥 Setting up HealthBridge Hospital on PythonAnywhere...

REM Configuration
set PYTHONANYWHERE_USERNAME=pratikshyabhattarai
set PYTHONANYWHERE_HOST=pythonanywhere.com
set PROJECT_NAME=health_bridge_hospital
set GITHUB_REPO=https://github.com/yourusername/health_bridge_hospital.git

REM Check if we're in the right directory
if not exist "package.json" (
    echo [ERROR] Please run this script from the project root directory
    pause
    exit /b 1
)

if not exist "backend" (
    echo [ERROR] Backend directory not found
    pause
    exit /b 1
)

REM Generate SSH key if it doesn't exist
if not exist "%USERPROFILE%\.ssh\pythonanywhere_key" (
    echo [INFO] Generating SSH key for PythonAnywhere...
    ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f "%USERPROFILE%\.ssh\pythonanywhere_key" -N ""
    echo [SUCCESS] SSH key generated successfully
    
    echo [WARNING] Please add the following public key to PythonAnywhere:
    echo ==========================================
    type "%USERPROFILE%\.ssh\pythonanywhere_key.pub"
    echo ==========================================
    echo.
    echo [INFO] Steps to add SSH key to PythonAnywhere:
    echo 1. Go to https://www.pythonanywhere.com
    echo 2. Log in with your account
    echo 3. Go to Account tab
    echo 4. Click on 'SSH keys'
    echo 5. Click 'Add a new key'
    echo 6. Paste the public key above
    echo 7. Click 'Add key'
    echo.
    pause
)

REM Test SSH connection
echo [INFO] Testing SSH connection to PythonAnywhere...
ssh -o ConnectTimeout=10 -o BatchMode=yes %PYTHONANYWHERE_USERNAME%@%PYTHONANYWHERE_HOST% exit
if errorlevel 1 (
    echo [ERROR] SSH connection failed. Please check your SSH key setup.
    pause
    exit /b 1
)

echo [SUCCESS] SSH connection successful

REM Setup project on PythonAnywhere
echo [INFO] Setting up project on PythonAnywhere...

ssh %PYTHONANYWHERE_USERNAME%@%PYTHONANYWHERE_HOST% "mkdir -p /home/pratikshyabhattarai/health_bridge_hospital && cd /home/pratikshyabhattarai/health_bridge_hospital && if not exist .git (git clone %GITHUB_REPO% .) else (git pull origin main) && cd backend && python3.10 -m venv venv && source venv/bin/activate && pip install --user -r requirements.txt && mkdir -p logs && cp env.example .env"

if errorlevel 1 (
    echo [ERROR] Setup failed. Please check the error messages above.
    pause
    exit /b 1
)

echo [SUCCESS] Initial setup completed successfully!
echo [INFO] Next steps:
echo 1. SSH into PythonAnywhere: ssh pratikshyabhattarai@pythonanywhere.com
echo 2. Navigate to project: cd /home/pratikshyabhattarai/health_bridge_hospital/backend
echo 3. Update .env file with your credentials
echo 4. Run: python manage.py migrate --settings=healthbridge_backend.settings_production
echo 5. Run: python manage.py createsuperuser --settings=healthbridge_backend.settings_production
echo 6. Run: python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
echo 7. Configure web app in PythonAnywhere dashboard

pause
