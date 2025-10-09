@echo off
echo ========================================
echo HealthBridge Hospital - Backend Only
echo ========================================
echo.

echo Starting Backend (Django) server...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo Please install Python from: https://python.org/
    pause
    exit /b 1
)

REM Navigate to backend directory
cd backend

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
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

if not exist "venv\Lib\site-packages\django" (
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating environment file...
    copy env.example .env
)

REM Start Django server
echo Starting Django server...
echo.
echo Backend API: http://localhost:8000
echo Admin Panel: http://localhost:8000/admin/
echo API Docs:    http://localhost:8000/api/docs/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 8000
