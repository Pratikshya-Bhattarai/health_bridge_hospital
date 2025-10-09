@echo off
echo ========================================
echo HealthBridge Hospital - Frontend Only
echo ========================================
echo.

echo Starting Frontend (Next.js) server...
echo.

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed!
    echo Please install Node.js from: https://nodejs.org/
    pause
    exit /b 1
)

REM Install dependencies if needed
if not exist "node_modules" (
    echo Installing dependencies...
    npm install
)

REM Start development server
echo Starting development server...
echo.
echo Your website will open at: http://localhost:3000
echo Press Ctrl+C to stop the server
echo.

start http://localhost:3000
npm run dev
