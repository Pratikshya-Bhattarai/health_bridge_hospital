@echo off
title HealthBridge Hospital - FIX EVERYTHING
color 0C
echo.
echo ========================================
echo 🏥 HealthBridge Hospital - FIX EVERYTHING
echo ========================================
echo.

REM Set working directory
cd /d "%~dp0"

echo This script will fix all common issues...
echo.

echo [FIX 1] Cleaning npm cache...
npm cache clean --force

echo [FIX 2] Removing node_modules...
if exist "node_modules" (
    rmdir /s /q "node_modules"
)

echo [FIX 3] Removing package-lock.json...
if exist "package-lock.json" (
    del "package-lock.json"
)

echo [FIX 4] Reinstalling dependencies...
npm install --force --legacy-peer-deps

echo [FIX 5] Cleaning Python cache...
if exist "backend" (
    cd backend
    if exist "__pycache__" (
        rmdir /s /q "__pycache__"
    )
    if exist "venv" (
        rmdir /s /q "venv"
    )
    cd ..
)

echo.
echo ✅ All fixes applied!
echo.
echo Now run MAKE_IT_WORK.bat to start everything.
echo.
pause
