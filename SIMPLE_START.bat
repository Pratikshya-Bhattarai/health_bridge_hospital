@echo off
echo Starting HealthBridge Hospital...
echo.

REM Check if we're in the right directory
if not exist "package.json" (
    echo ERROR: package.json not found!
    echo Make sure you're in the correct directory.
    pause
    exit /b 1
)

REM Try to start the server
echo Attempting to start the server...
echo.

REM Method 1: Try npm run dev
echo Trying: npm run dev
npm run dev

REM If that fails, try alternative
if %errorlevel% neq 0 (
    echo.
    echo npm run dev failed, trying alternative...
    echo.
    
    REM Try installing dependencies first
    echo Installing dependencies...
    npm install
    
    REM Try again
    echo Trying again...
    npm run dev
)

echo.
echo If you see errors above, please share them.
pause
