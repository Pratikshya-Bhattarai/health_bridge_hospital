@echo off
echo ========================================
echo HealthBridge Hospital - Frontend Server
echo ========================================
echo.

echo Checking system requirements...

REM Check if Node.js is installed
echo [1/4] Checking Node.js installation...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Node.js is not installed!
    echo.
    echo Please install Node.js from: https://nodejs.org/
    echo Choose the LTS version and restart your terminal.
    echo.
    echo After installing Node.js, run this script again.
    echo.
    pause
    exit /b 1
)
echo ✅ Node.js is installed!

REM Check if npm is working
echo [2/4] Checking npm...
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: npm is not working!
    echo Please reinstall Node.js from: https://nodejs.org/
    pause
    exit /b 1
)
echo ✅ npm is working!

REM Install dependencies if needed
echo [3/4] Checking dependencies...
if not exist "node_modules" (
    echo Installing dependencies (this may take a few minutes)...
    npm install
    if %errorlevel% neq 0 (
        echo ❌ ERROR: Failed to install dependencies!
        echo Please check your internet connection and try again.
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed successfully!
) else (
    echo ✅ Dependencies already installed!
)

REM Start development server
echo [4/4] Starting development server...
echo.
echo ========================================
echo 🚀 Starting HealthBridge Hospital Website
echo ========================================
echo.
echo Your website will open at: http://localhost:3000
echo Press Ctrl+C to stop the server
echo.
echo Opening browser in 3 seconds...
timeout /t 3 /nobreak >nul

start http://localhbuild backend in python django (ask it to use supabase db)
create proper api for booking (with good documentation)
 
ost:3000
npm run dev
