# 🏥 HealthBridge Hospital - Complete Deployment Guide

## 📋 Overview

This comprehensive guide will help you deploy your HealthBridge Hospital application to PythonAnywhere with automated GitHub deployment. The application consists of:

- **Frontend**: Next.js application (deployed to Vercel)
- **Backend**: Django REST API (deployed to PythonAnywhere)
- **Database**: Supabase PostgreSQL
- **Automated Deployment**: GitHub Actions

## 🎯 Deployment Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   GitHub Repo   │    │  PythonAnywhere │    │    Supabase     │
│                 │    │                 │    │   Database      │
│  ┌───────────┐  │    │  ┌───────────┐  │    │                 │
│  │   Code    │──┼────┼──│  Django   │──┼────│   PostgreSQL    │
│  │           │  │    │  │   API     │  │    │                 │
│  └───────────┘  │    │  └───────────┘  │    └─────────────────┘
└─────────────────┘    └─────────────────┘
         │                       │
         │                       │
         ▼                       ▼
┌─────────────────┐    ┌─────────────────┐
│     Vercel      │    │   Your Domain    │
│   (Frontend)    │    │  bepratikshya.   │
│                 │    │ pythonanywhere.  │
│  Next.js App    │    │      com         │
└─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start (5 Minutes)

### Prerequisites

- GitHub account
- PythonAnywhere account (free tier)
- Supabase account
- Git installed on your local machine

### Step 1: GitHub Repository Setup

1. **Create a new repository on GitHub:**
   - Go to [github.com](https://github.com)
   - Click "New repository"
   - Name: `health_bridge_hospital`
   - Make it public
   - Don't initialize with README

2. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - HealthBridge Hospital"
   git branch -M main
   git remote add origin https://github.com/yourusername/health_bridge_hospital.git
   git push -u origin main
   ```

### Step 2: PythonAnywhere Account Setup

1. **Sign up for PythonAnywhere:**
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Create a free "Beginner" account
   - Username: `bepratikshya` (or your choice)
   - Remember your password!

2. **Create API Token:**
   - Go to Account tab
   - Click "API token"
   - Click "Create new API token"
   - Save the token somewhere safe

### Step 3: Supabase Database Setup

1. **Create Supabase project:**
   - Go to [supabase.com](https://supabase.com)
   - Create new project
   - Choose a region close to your users
   - Set a strong database password

2. **Get database credentials:**
   - Go to Settings → Database
   - Copy the connection details:
     - Host
     - Database name
     - Username
     - Password
     - Port (usually 5432)

### Step 4: SSH Key Setup

1. **Generate SSH key (if you don't have one):**
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your-email@example.com" -f ~/.ssh/pythonanywhere_key
   ```

2. **Add public key to PythonAnywhere:**
   ```bash
   cat ~/.ssh/pythonanywhere_key.pub
   ```
   - Copy the output
   - Go to PythonAnywhere → Account → SSH keys
   - Add new key
   - Paste the public key

3. **Test SSH connection:**
   ```bash
   ssh bepratikshya@pythonanywhere.com
   ```

### Step 5: Initial PythonAnywhere Setup

1. **SSH into PythonAnywhere:**
   ```bash
   ssh bepratikshya@pythonanywhere.com
   ```

2. **Clone your repository:**
   ```bash
   git clone https://github.com/yourusername/health_bridge_hospital.git
   cd health_bridge_hospital/backend
   ```

3. **Set up virtual environment:**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --user -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp env.example .env
   nano .env
   ```

   **Update .env with your credentials:**
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=bepratikshya.pythonanywhere.com,www.bepratikshya.pythonanywhere.com
   
   # Database Configuration (Supabase)
   DB_NAME=your-supabase-db-name
   DB_USER=your-supabase-user
   DB_PASSWORD=your-supabase-password
   DB_HOST=db.your-project.supabase.co
   DB_PORT=5432
   
   # Supabase Configuration
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-supabase-anon-key
   SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
   
   # JWT Settings
   JWT_SECRET_KEY=your-jwt-secret-key
   JWT_ALGORITHM=HS256
   JWT_ACCESS_TOKEN_LIFETIME=60
   JWT_REFRESH_TOKEN_LIFETIME=1440
   
   # Email Configuration
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

5. **Run initial setup:**
   ```bash
   python manage.py migrate --settings=healthbridge_backend.settings_production
   python manage.py createsuperuser --settings=healthbridge_backend.settings_production
   python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
   ```

### Step 6: Configure Web App

1. **Go to PythonAnywhere Web tab**
2. **Add a new web app:**
   - Choose "Manual Configuration"
   - Choose "Python 3.10"
   - Click "Next"

3. **Configure WSGI file:**
   - File: `/var/www/bepratikshya_pythonanywhere_com_wsgi.py`
   ```python
   import os
   import sys
   
   path = '/home/bepratikshya/health_bridge_hospital/backend'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'
   
   activate_this = '/home/bepratikshya/health_bridge_hospital/backend/venv/bin/activate_this.py'
   if os.path.exists(activate_this):
       exec(open(activate_this).read(), dict(__file__=activate_this))
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

4. **Configure static files:**
   - **URL:** `/static/`
   - **Directory:** `/home/bepratikshya/health_bridge_hospital/backend/staticfiles`
   - **URL:** `/media/`
   - **Directory:** `/home/bepratikshya/health_bridge_hospital/backend/media`

5. **Reload web app**

### Step 7: GitHub Actions Setup

1. **Add GitHub Secrets:**
   - Go to your GitHub repository
   - Settings → Secrets and variables → Actions
   - Add these secrets:
     ```
     PYTHONANYWHERE_HOST: pythonanywhere.com
     PYTHONANYWHERE_USERNAME: bepratikshya
     PYTHONANYWHERE_SSH_KEY: [Your private SSH key]
     ```

2. **Get your private SSH key:**
   ```bash
   cat ~/.ssh/pythonanywhere_key
   ```
   - Copy the entire content (including -----BEGIN and -----END lines)
   - Add it as `PYTHONANYWHERE_SSH_KEY` secret

### Step 8: Test Your Deployment

1. **Visit your site:**
   - `https://bepratikshya.pythonanywhere.com`
   - `https://bepratikshya.pythonanywhere.com/api/`
   - `https://bepratikshya.pythonanywhere.com/admin/`

2. **Test API endpoints:**
   ```bash
   curl https://bepratikshya.pythonanywhere.com/api/
   curl https://bepratikshya.pythonanywhere.com/api/appointments/
   ```

## 🔄 Automated Deployment

Once set up, every push to `main` branch will automatically deploy:

```bash
git add .
git commit -m "Update feature"
git push origin main
```

GitHub Actions will:
1. Connect to PythonAnywhere via SSH
2. Pull latest changes
3. Update dependencies
4. Run migrations
5. Collect static files
6. Restart the web app

## 🛠️ Manual Deployment

If you need to deploy manually:

```bash
# SSH into PythonAnywhere
ssh bepratikshya@pythonanywhere.com

# Navigate to project
cd /home/bepratikshya/health_bridge_hospital

# Pull changes
git pull origin main

# Deploy
cd backend
source venv/bin/activate
pip install --user -r requirements.txt
python manage.py migrate --settings=healthbridge_backend.settings_production
python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
touch /var/www/bepratikshya_pythonanywhere_com_wsgi.py
```

## 🔧 Troubleshooting

### Common Issues:

1. **SSH Connection Failed:**
   - Check SSH key is added to PythonAnywhere
   - Verify GitHub secrets are correct
   - Test: `ssh bepratikshya@pythonanywhere.com`

2. **Environment Variables Not Loading:**
   - Check .env file exists and has correct values
   - Verify file permissions: `chmod 600 .env`

3. **Database Connection Issues:**
   - Verify Supabase credentials in .env
   - Check database host and port
   - Test connection: `python manage.py dbshell --settings=healthbridge_backend.settings_production`

4. **Static Files Not Loading:**
   - Run: `python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production`
   - Check static file mappings in PythonAnywhere Web tab

5. **Import Errors:**
   - Check all dependencies are installed: `pip install --user -r requirements.txt`
   - Verify virtual environment is activated

### Useful Commands:

```bash
# Check logs
tail -f /var/log/bepratikshya.pythonanywhere.com.error.log

# Check Django logs
tail -f /home/bepratikshya/health_bridge_hospital/backend/logs/django.log

# Test Django setup
python manage.py check --deploy --settings=healthbridge_backend.settings_production

# Check environment variables
python manage.py shell --settings=healthbridge_backend.settings_production -c "import os; print(os.environ.get('SECRET_KEY'))"

# Check database connection
python manage.py dbshell --settings=healthbridge_backend.settings_production
```

## 📊 Your Live API

After successful deployment:

- **Base URL:** `https://bepratikshya.pythonanywhere.com/api/`
- **Appointments:** `https://bepratikshya.pythonanywhere.com/api/appointments/`
- **Doctors:** `https://bepratikshya.pythonanywhere.com/api/doctors/`
- **Patients:** `https://bepratikshya.pythonanywhere.com/api/patients/`
- **Admin:** `https://bepratikshya.pythonanywhere.com/admin/`

## 🎯 Next Steps

1. **Update frontend** to use production API URL
2. **Set up monitoring** and alerts
3. **Configure backups** for your database
4. **Set up custom domain** (optional)
5. **Implement SSL certificate** (PythonAnywhere provides this automatically)

## 📞 Support

- **PythonAnywhere Help:** [help.pythonanywhere.com](https://help.pythonanywhere.com)
- **GitHub Actions:** [docs.github.com/actions](https://docs.github.com/en/actions)
- **Django Deployment:** [docs.djangoproject.com](https://docs.djangoproject.com/en/stable/howto/deployment/)
- **Supabase Docs:** [supabase.com/docs](https://supabase.com/docs)

## 🎉 Success!

Your HealthBridge Hospital backend is now live on PythonAnywhere with automated deployment!

**Your API is available at:**
`https://bepratikshya.pythonanywhere.com/api/`

**Update your frontend to use this URL for production!**

---

## 📝 Quick Reference

### Essential Commands:
```bash
# Deploy manually
ssh bepratikshya@pythonanywhere.com
cd /home/bepratikshya/health_bridge_hospital/backend
source venv/bin/activate
git pull origin main
pip install --user -r requirements.txt
python manage.py migrate --settings=healthbridge_backend.settings_production
python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
touch /var/www/bepratikshya_pythonanywhere_com_wsgi.py
```

### Important Files:
- `.env` - Environment variables
- `backend/healthbridge_backend/settings_production.py` - Production settings
- `.github/workflows/deploy.yml` - GitHub Actions workflow
- `/var/www/bepratikshya_pythonanywhere_com_wsgi.py` - WSGI configuration

### Key URLs:
- **Your Site:** https://bepratikshya.pythonanywhere.com
- **API:** https://bepratikshya.pythonanywhere.com/api/
- **Admin:** https://bepratikshya.pythonanywhere.com/admin/
- **PythonAnywhere Dashboard:** https://www.pythonanywhere.com
