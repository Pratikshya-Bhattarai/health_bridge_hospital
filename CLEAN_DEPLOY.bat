@echo off
title HealthBridge Hospital - Clean Deploy
color 0A

echo.
echo ████████████████████████████████████████████████████████████████████████████████
echo ██                                                                        ██
echo ██                    🚀 HealthBridge Hospital - Clean Deploy 🚀         ██
echo ██                                                                        ██
echo ████████████████████████████████████████████████████████████████████████████████
echo.

echo 🎯 DEPLOYMENT PROCESS:
echo.
echo ✅ Step 1: Set up PythonAnywhere (Backend)
echo    → Go to: https://www.pythonanywhere.com
echo    → Sign up for free account
echo    → Create API token in Account settings
echo    → Save the API token!
echo.

echo ✅ Step 2: Set up Supabase Database
echo    → Go to: https://supabase.com
echo    → Create new project: healthbridge-hospital
echo    → Get database connection details
echo    → Save the password and host!
echo.

echo ✅ Step 3: Configure GitHub Secrets
echo    → Go to: https://github.com/Pratikshya-Bhattarai/health_bridge_hospital/settings/secrets/actions
echo    → Add these secrets:
echo       - PYTHONANYWHERE_API_TOKEN = [Your PythonAnywhere API Token]
echo       - PYTHONANYWHERE_USERNAME = bepratikshya
echo       - DB_NAME = postgres
echo       - DB_USER = postgres
echo       - DB_PASSWORD = [Your Supabase Password]
echo       - DB_HOST = [Your Supabase Host]
echo       - DB_PORT = 5432
echo       - SECRET_KEY = djangosecretkey2024!@#$%^&*(-_=+)abcdefghijklmnopqrstuvwxyz0123456789
echo.

echo ✅ Step 4: Deploy Frontend to Vercel
echo    → Go to: https://vercel.com
echo    → Import your GitHub repository
echo    → Set environment variable: NEXT_PUBLIC_API_URL = https://bepratikshya.pythonanywhere.com
echo.

echo 🎉 FINAL URLs (after deployment):
echo    Backend API: https://bepratikshya.pythonanywhere.com
echo    Frontend: https://your-vercel-app.vercel.app
echo    Admin Panel: https://bepratikshya.pythonanywhere.com/admin/
echo.

echo 🚀 Ready to start deployment? Press any key to begin...
pause >nul

echo.
echo 📋 Opening deployment resources...
start https://www.pythonanywhere.com
start https://supabase.com
start https://github.com/Pratikshya-Bhattarai/health_bridge_hospital/settings/secrets/actions
start https://vercel.com

echo.
echo 🎯 Follow the steps above to complete your deployment!
echo 📖 For detailed instructions, see: DEPLOYMENT_CHECKLIST.md
echo.
pause
