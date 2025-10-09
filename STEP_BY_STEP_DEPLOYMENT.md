# 🚀 HealthBridge Hospital - Step-by-Step Deployment Guide

## 📋 Prerequisites

Before starting, make sure you have:
- ✅ GitHub account
- ✅ Git installed on your computer
- ✅ Your code pushed to GitHub (already done!)

## 🎯 Deployment Architecture

Your application will be deployed as follows:
- **Frontend (Next.js)**: Vercel (free hosting)
- **Backend (Django)**: PythonAnywhere (free hosting)
- **Database**: Supabase (free PostgreSQL database)

## 🚀 Step 1: Set up PythonAnywhere (Backend)

### 1.1 Create PythonAnywhere Account
1. Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Click "Sign up for a free account"
3. Choose your username carefully - this will be your domain: `username.pythonanywhere.com`
4. Complete the signup process

### 1.2 Create API Token
1. After signup, go to your **Account** page
2. Click on the **API token** tab
3. Click **"Create new API token"**
4. **Save this token** - you'll need it for GitHub Actions

### 1.3 Configure Your Web App
1. Go to the **Web** tab in PythonAnywhere
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **Python 3.10**
5. Click **"Next"**

## 🗄️ Step 2: Set up Supabase Database

### 2.1 Create Supabase Project
1. Go to [https://supabase.com](https://supabase.com)
2. Sign up for a free account
3. Click **"New Project"**
4. Choose your organization
5. Enter project details:
   - **Name**: `healthbridge-hospital`
   - **Database Password**: Create a strong password
   - **Region**: Choose closest to your users
6. Click **"Create new project"**

### 2.2 Get Database Connection Details
1. Go to **Settings** → **Database**
2. Copy these details:
   - **Host**: `db.xxxxxxxxxxxxx.supabase.co`
   - **Database name**: `postgres`
   - **Port**: `5432`
   - **User**: `postgres`
   - **Password**: (the one you created)

## 🔐 Step 3: Configure GitHub Secrets

### 3.1 Add Repository Secrets
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Add these secrets one by one:

```
PYTHONANYWHERE_API_TOKEN = [Your PythonAnywhere API Token]
PYTHONANYWHERE_USERNAME = [Your PythonAnywhere Username]
DB_NAME = postgres
DB_USER = postgres
DB_PASSWORD = [Your Supabase Database Password]
DB_HOST = [Your Supabase Database Host]
DB_PORT = 5432
SECRET_KEY = [Generate a new Django secret key]
```

### 3.2 Generate Django Secret Key
Run this command to generate a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 🌐 Step 4: Deploy Frontend to Vercel

### 4.1 Connect to Vercel
1. Go to [https://vercel.com](https://vercel.com)
2. Sign up with your GitHub account
3. Click **"New Project"**
4. Import your `health_bridge_hospital` repository

### 4.2 Configure Vercel Settings
1. **Framework Preset**: Next.js
2. **Root Directory**: Leave empty (it's the root)
3. **Build Command**: `npm run build`
4. **Output Directory**: `out`
5. **Install Command**: `npm install`

### 4.3 Add Environment Variables
In Vercel, go to **Settings** → **Environment Variables** and add:
```
NEXT_PUBLIC_API_URL = https://bepratikshya.pythonanywhere.com
```

### 4.4 Deploy
1. Click **"Deploy"**
2. Wait for the build to complete
3. Your frontend will be available at: `https://your-project-name.vercel.app`

## 🔄 Step 5: Trigger Backend Deployment

### 5.1 Push Changes to GitHub
```bash
git add .
git commit -m "Configure for deployment"
git push origin main
```

### 5.2 Monitor GitHub Actions
1. Go to your GitHub repository
2. Click on **Actions** tab
3. Watch the deployment workflow run
4. Check for any errors in the logs

## 🧪 Step 6: Test Your Deployment

### 6.1 Test Backend API
1. Visit: `https://bepratikshya.pythonanywhere.com/api/`
2. You should see your Django API documentation
3. Test endpoints like: `https://bepratikshya.pythonanywhere.com/api/doctors/`

### 6.2 Test Frontend
1. Visit your Vercel URL
2. Check if the frontend loads correctly
3. Test the connection between frontend and backend

### 6.3 Test Database Connection
1. Go to PythonAnywhere → **Web** tab
2. Click on your web app
3. Check the **Error log** for any database connection issues

## 🔧 Troubleshooting

### Common Issues:

#### Backend Not Working
- Check PythonAnywhere error logs
- Verify database connection settings
- Ensure all environment variables are set

#### Frontend Not Connecting to Backend
- Check CORS settings in Django
- Verify API URL in frontend environment variables
- Test API endpoints directly

#### Database Connection Issues
- Verify Supabase connection details
- Check if database is accessible from PythonAnywhere
- Ensure SSL is enabled for Supabase

## 📱 Step 7: Create Admin User

### 7.1 Access PythonAnywhere Console
1. Go to **Consoles** tab
2. Start a **Bash** console
3. Navigate to your project directory

### 7.2 Create Superuser
```bash
cd /home/bepratikshya/health_bridge_hospital/backend
python manage.py createsuperuser
```

### 7.3 Access Admin Panel
1. Go to: `https://bepratikshya.pythonanywhere.com/admin/`
2. Login with your superuser credentials
3. Add some test data

## 🎉 Success!

Your HealthBridge Hospital application is now live!

- **Backend API**: `https://bepratikshya.pythonanywhere.com`
- **Frontend**: `https://your-vercel-app.vercel.app`
- **Admin Panel**: `https://bepratikshya.pythonanywhere.com/admin/`

## 🔄 Future Updates

To update your application:
1. Make changes locally
2. Commit and push to GitHub
3. GitHub Actions will automatically deploy to PythonAnywhere
4. Vercel will automatically deploy frontend changes

## 📞 Support

If you encounter any issues:
1. Check the error logs in PythonAnywhere
2. Check GitHub Actions logs
3. Verify all environment variables are set correctly
4. Test database connectivity

---

**Congratulations! Your HealthBridge Hospital application is now live on the internet! 🎉**
