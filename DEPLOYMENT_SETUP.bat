@echo off
echo ========================================
echo HealthBridge Hospital - Deployment Setup
echo ========================================
echo.

echo Step 1: Setting up PythonAnywhere...
echo.
echo 1. Go to https://www.pythonanywhere.com
echo 2. Sign up for a free account
echo 3. Choose your username (this will be your domain: username.pythonanywhere.com)
echo 4. After signup, go to Account page and create an API token
echo.
pause

echo Step 2: Setting up Supabase Database...
echo.
echo 1. Go to https://supabase.com
echo 2. Create a new project
echo 3. Go to Settings > Database
echo 4. Copy the connection details
echo.
pause

echo Step 3: Setting up GitHub Secrets...
echo.
echo Go to your GitHub repository settings and add these secrets:
echo.
echo PYTHONANYWHERE_API_TOKEN = [Your PythonAnywhere API Token]
echo PYTHONANYWHERE_USERNAME = [Your PythonAnywhere Username]
echo DB_NAME = [Your Supabase Database Name]
echo DB_USER = [Your Supabase Database User]
echo DB_PASSWORD = [Your Supabase Database Password]
echo DB_HOST = [Your Supabase Database Host]
echo DB_PORT = 5432
echo SECRET_KEY = [Generate a new Django secret key]
echo.
pause

echo Step 4: Deploying Frontend to Vercel...
echo.
echo 1. Go to https://vercel.com
echo 2. Sign up with GitHub
echo 3. Import your repository
echo 4. Set build command: npm run build
echo 5. Set output directory: out
echo 6. Add environment variable: NEXT_PUBLIC_API_URL=https://bepratikshya.pythonanywhere.com
echo.
pause

echo Step 5: Testing Deployment...
echo.
echo 1. Check your backend: https://bepratikshya.pythonanywhere.com/api/
echo 2. Check your frontend: https://your-vercel-app.vercel.app
echo 3. Test the connection between frontend and backend
echo.
pause

echo Deployment setup complete!
echo.
echo Your application will be available at:
echo - Backend API: https://bepratikshya.pythonanywhere.com
echo - Frontend: https://your-vercel-app.vercel.app
echo.
pause
