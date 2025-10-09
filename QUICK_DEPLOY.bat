@echo off
title HealthBridge Hospital - Quick Deploy
color 0A

echo.
echo ████████████████████████████████████████████████████████████████████████████████
echo ██                                                                        ██
echo ██                    🏥 HealthBridge Hospital Deployment 🏥                ██
echo ██                                                                        ██
echo ████████████████████████████████████████████████████████████████████████████████
echo.

echo 📋 DEPLOYMENT CHECKLIST:
echo.
echo ✅ 1. GitHub Repository: https://github.com/Pratikshya-Bhattarai/health_bridge_hospital
echo ✅ 2. Code pushed to GitHub
echo.
echo 🔄 NEXT STEPS:
echo.
echo 📝 Step 1: Set up PythonAnywhere
echo    → Go to: https://www.pythonanywhere.com
echo    → Sign up for free account
echo    → Create API token in Account settings
echo.
echo 📝 Step 2: Set up Supabase Database
echo    → Go to: https://supabase.com
echo    → Create new project
echo    → Get database connection details
echo.
echo 📝 Step 3: Configure GitHub Secrets
echo    → Go to: https://github.com/Pratikshya-Bhattarai/health_bridge_hospital/settings/secrets/actions
echo    → Add these secrets:
echo       - PYTHONANYWHERE_API_TOKEN
echo       - PYTHONANYWHERE_USERNAME
echo       - DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
echo       - SECRET_KEY
echo.
echo 📝 Step 4: Deploy Frontend to Vercel
echo    → Go to: https://vercel.com
echo    → Import your GitHub repository
echo    → Set environment variable: NEXT_PUBLIC_API_URL
echo.
echo 📝 Step 5: Test Deployment
echo    → Backend: https://bepratikshya.pythonanywhere.com
echo    → Frontend: https://your-vercel-app.vercel.app
echo.

echo 📖 For detailed instructions, see: STEP_BY_STEP_DEPLOYMENT.md
echo.

echo 🚀 Ready to deploy? Press any key to open the deployment guide...
pause >nul

start notepad STEP_BY_STEP_DEPLOYMENT.md

echo.
echo 🎯 Deployment URLs (after setup):
echo    Backend API: https://bepratikshya.pythonanywhere.com
echo    Frontend: https://your-vercel-app.vercel.app
echo    Admin Panel: https://bepratikshya.pythonanywhere.com/admin/
echo.

echo 📞 Need help? Check the deployment guides in your project folder!
echo.
pause
