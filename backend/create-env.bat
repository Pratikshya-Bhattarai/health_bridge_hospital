@echo off
echo ========================================
echo   Creating Environment Variables File
echo ========================================
echo.

echo Creating .env file for PythonAnywhere deployment...
echo.

echo Please enter your Supabase credentials:
echo.

set /p SUPABASE_URL="Enter your Supabase URL: "
set /p SUPABASE_KEY="Enter your Supabase Key: "
set /p DB_NAME="Enter your Database Name: "
set /p DB_USER="Enter your Database User: "
set /p DB_PASSWORD="Enter your Database Password: "
set /p DB_HOST="Enter your Database Host: "

echo.
echo Creating .env file...

(
echo # HealthBridge Backend Environment Variables
echo # For PythonAnywhere Deployment
echo.
echo SECRET_KEY=your-secret-key-change-this-in-production
echo DEBUG=False
echo.
echo # Supabase Configuration
echo SUPABASE_URL=%SUPABASE_URL%
echo SUPABASE_KEY=%SUPABASE_KEY%
echo.
echo # Database Configuration
echo DB_NAME=%DB_NAME%
echo DB_USER=%DB_USER%
echo DB_PASSWORD=%DB_PASSWORD%
echo DB_HOST=%DB_HOST%
echo DB_PORT=5432
echo.
echo # Email Configuration ^(Optional^)
echo EMAIL_HOST_USER=
echo EMAIL_HOST_PASSWORD=
) > .env

echo.
echo ✅ .env file created successfully!
echo.
echo 📋 Next steps:
echo    1. Upload this .env file to PythonAnywhere
echo    2. Place it in your backend directory
echo    3. Make sure to keep it secure
echo.
echo ⚠️  Important: Never commit .env to git!
echo.
pause
