# ✅ HealthBridge Hospital - Deployment Checklist

## 🎯 Pre-Deployment Setup

### 1. PythonAnywhere Setup
- [ ] Go to https://www.pythonanywhere.com
- [ ] Sign up for free account
- [ ] Choose username: `bepratikshya` (or your preferred username)
- [ ] Go to Account → API token → Create new API token
- [ ] **Save the API token!**

### 2. Supabase Database Setup
- [ ] Go to https://supabase.com
- [ ] Sign up for free account
- [ ] Create new project: `healthbridge-hospital`
- [ ] Set strong database password
- [ ] Go to Settings → Database
- [ ] **Copy these details:**
  - Host: `db.xxxxxxxxxxxxx.supabase.co`
  - Database: `postgres`
  - Port: `5432`
  - User: `postgres`
  - Password: `[your password]`

### 3. GitHub Secrets Setup
- [ ] Go to: https://github.com/Pratikshya-Bhattarai/health_bridge_hospital/settings/secrets/actions
- [ ] Add these secrets:

#### Required Secrets:
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

## 🚀 Deployment Process

### 4. Trigger Backend Deployment
- [ ] Push changes to GitHub (already done!)
- [ ] Go to GitHub Actions tab
- [ ] Watch the deployment workflow run
- [ ] Check for any errors in logs

### 5. Deploy Frontend to Vercel
- [ ] Go to https://vercel.com
- [ ] Sign up with GitHub account
- [ ] Click "New Project"
- [ ] Import `health_bridge_hospital` repository
- [ ] Configure settings:
  - Framework: Next.js
  - Build Command: `npm run build`
  - Output Directory: `out`
- [ ] Add environment variable:
  - `NEXT_PUBLIC_API_URL = https://bepratikshya.pythonanywhere.com`
- [ ] Click "Deploy"

## 🧪 Testing & Verification

### 6. Test Backend API
- [ ] Visit: https://bepratikshya.pythonanywhere.com/api/
- [ ] Should see Django API documentation
- [ ] Test endpoint: https://bepratikshya.pythonanywhere.com/api/doctors/

### 7. Test Frontend
- [ ] Visit your Vercel URL
- [ ] Check if frontend loads correctly
- [ ] Test navigation and features

### 8. Test Database Connection
- [ ] Go to PythonAnywhere → Web tab
- [ ] Check error logs for database issues
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Test admin panel: https://bepratikshya.pythonanywhere.com/admin/

## 🎉 Final URLs

After successful deployment:
- **Backend API**: https://bepratikshya.pythonanywhere.com
- **Frontend**: https://your-vercel-app.vercel.app
- **Admin Panel**: https://bepratikshya.pythonanywhere.com/admin/

## 🔧 Troubleshooting

### Common Issues:
- **Backend not working**: Check PythonAnywhere error logs
- **Database connection**: Verify Supabase settings
- **Frontend not connecting**: Check CORS settings and API URL
- **Build failures**: Check GitHub Actions logs

### Quick Fixes:
- Restart PythonAnywhere web app
- Check all environment variables are set
- Verify database is accessible
- Test API endpoints directly

## 📞 Need Help?

1. Check error logs in PythonAnywhere
2. Check GitHub Actions logs
3. Verify all secrets are set correctly
4. Test database connectivity
5. Check CORS settings

---

**🎯 Goal**: Get your HealthBridge Hospital application live on the internet!
