@echo off
title HealthBridge Hospital - DEBUG
color 0E
echo.
echo ========================================
echo 🏥 HealthBridge Hospital - DEBUG MODE
echo ========================================
echo.

REM Set working directory
cd /d "%~dp0"
echo Current directory: %CD%
echo.

echo [DEBUG 1] Checking if files exist...
if exist "package.json" (
    echo ✅ package.json found
) else (
    echo ❌ package.json NOT found
)

if exist "node_modules" (
    echo ✅ node_modules found
) else (
    echo ❌ node_modules NOT found
)

echo.
echo [DEBUG 2] Checking Node.js...
node --version
if %errorlevel% neq 0 (
    echo ❌ Node.js command failed
    echo Error code: %errorlevel%
) else (
    echo ✅ Node.js is working
)

echo.
echo [DEBUG 3] Checking npm...
npm --version
if %errorlevel% neq 0 (
    echo ❌ npm command failed
    echo Error code: %errorlevel%
) else (
    echo ✅ npm is working
)

echo.
echo [DEBUG 4] Testing npm install...
echo Running: npm install --dry-run
npm install --dry-run
echo Exit code: %errorlevel%

echo.
echo [DEBUG 5] Checking network...
ping -n 1 google.com >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ No internet connection
) else (
    echo ✅ Internet connection working
)

echo.
echo [DEBUG 6] Checking permissions...
echo Testing file creation...
echo test > test_file.txt
if exist "test_file.txt" (
    echo ✅ File creation works
    del test_file.txt
) else (
    echo ❌ Cannot create files (permission issue)
)

echo.
echo ========================================
echo DEBUG COMPLETE
echo ========================================
echo.
echo If you see any ❌ errors above, that's the problem!
echo.
echo Common solutions:
echo 1. Run as Administrator (right-click - Run as administrator)
echo 2. Install Node.js from https://nodejs.org/
echo 3. Check internet connection
echo 4. Disable antivirus temporarily
echo.
pause
