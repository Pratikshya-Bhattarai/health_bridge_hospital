@echo off
REM HealthBridge Hospital - PythonAnywhere Deployment Script for Windows
REM This script automates the deployment process to PythonAnywhere

echo 🚀 Starting HealthBridge Hospital Deployment to PythonAnywhere...

REM Configuration
set PYTHONANYWHERE_USERNAME=pratikshyabhattarai
set PYTHONANYWHERE_HOST=pythonanywhere.com
set PROJECT_NAME=health_bridge_hospital
set BACKEND_DIR=backend

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

REM Check if SSH key exists
if not exist "%USERPROFILE%\.ssh\pythonanywhere_key" (
    echo [WARNING] SSH key not found. Please generate one first:
    echo.
    echo ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f %USERPROFILE%\.ssh\pythonanywhere_key
    echo.
    echo Then add the public key to PythonAnywhere:
    echo type %USERPROFILE%\.ssh\pythonanywhere_key.pub
    echo.
    pause
    exit /b 1
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

REM Deploy to PythonAnywhere
echo [INFO] Deploying to PythonAnywhere...

ssh %PYTHONANYWHERE_USERNAME%@%PYTHONANYWHERE_HOST% "cd /home/pratikshyabhattarai/health_bridge_hospital && git pull origin main && cd backend && source venv/bin/activate && pip install --user -r requirements.txt && python manage.py migrate --settings=healthbridge_backend.settings_production && python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production && touch /var/www/pratikshyabhattarai_pythonanywhere_com_wsgi.py"

if errorlevel 1 (
    echo [ERROR] Deployment failed. Please check the error messages above.
    pause
    exit /b 1
)

echo [SUCCESS] Deployment completed successfully!
echo [INFO] Your application is now live at: https://pratikshyabhattarai.pythonanywhere.com
echo [INFO] API endpoint: https://pratikshyabhattarai.pythonanywhere.com/api/
echo [INFO] Admin panel: https://pratikshyabhattarai.pythonanywhere.com/admin/

pause