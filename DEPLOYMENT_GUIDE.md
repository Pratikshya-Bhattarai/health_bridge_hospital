# 🚀 HealthBridge Hospital - Deployment Guide

## 🎯 Quick Deployment Steps

### Step 1: Set up PythonAnywhere (Backend)
1. Go to: https://www.pythonanywhere.com
2. Sign up for free account
3. Choose username: `bepratikshya`
4. Go to Account → API token → Create new API token
5. **Save the API token!**

### Step 2: Set up Supabase Database
1. Go to: https://supabase.com
2. Create new project: `healthbridge-hospital`
3. Set strong database password
4. Go to Settings → Database
5. **Copy these details:**
   - Host: `db.xxxxxxxxxxxxx.supabase.co`
   - Database: `postgres`
   - Port: `5432`
   - User: `postgres`
   - Password: (the one you created)

### Step 3: Configure GitHub Secrets
1. Go to: https://github.com/Pratikshya-Bhattarai/health_bridge_hospital/settings/secrets/actions
2. Add these secrets:

```
PYTHONANYWHERE_API_TOKEN = [Your PythonAnywhere API Token]
PYTHONANYWHERE_USERNAME = bepratikshya
DB_NAME = postgres
DB_USER = postgres
DB_PASSWORD = [Your Supabase Password]
DB_HOST = [Your Supabase Host]
DB_PORT = 5432
SECRET_KEY = djangosecretkey2024!@#$%^&*(-_=+)abcdefghijklmnopqrstuvwxyz0123456789
```

### Step 4: Deploy Frontend to Vercel
1. Go to: https://vercel.com
2. Import your GitHub repository
3. Set environment variable: `NEXT_PUBLIC_API_URL = https://bepratikshya.pythonanywhere.com`
4. Deploy!

## 🎉 Final URLs
- **Backend API**: https://bepratikshya.pythonanywhere.com
- **Frontend**: https://your-vercel-app.vercel.app
- **Admin Panel**: https://bepratikshya.pythonanywhere.com/admin/

## 🔧 Troubleshooting
- Check PythonAnywhere error logs
- Verify all GitHub secrets are set
- Test database connectivity
- Check CORS settings

---

**Ready to deploy? Follow the steps above!**
