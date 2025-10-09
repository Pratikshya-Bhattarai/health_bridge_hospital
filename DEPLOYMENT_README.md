# 🚀 HealthBridge Hospital - Deployment Guide

## 📋 Quick Overview

This guide will help you deploy your HealthBridge Hospital application to the cloud. The application consists of:

- **Frontend**: Next.js (deployed to Vercel)
- **Backend**: Django API (deployed to PythonAnywhere)
- **Database**: Supabase PostgreSQL
- **Automated Deployment**: GitHub Actions

## 🎯 What You'll Learn

1. How to set up GitHub repository
2. How to configure PythonAnywhere
3. How to set up Supabase database
4. How to configure automated deployment
5. How to troubleshoot common issues

## ⚡ Quick Start (5 Minutes)

### Step 1: GitHub Setup

1. **Create GitHub repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - HealthBridge Hospital"
   git branch -M main
   git remote add origin https://github.com/yourusername/health_bridge_hospital.git
   git push -u origin main
   ```

2. **Add GitHub Secrets:**
   - Go to Settings → Secrets and variables → Actions
   - Add these secrets:
     ```
     PYTHONANYWHERE_HOST: pythonanywhere.com
     PYTHONANYWHERE_USERNAME: bepratikshya
     PYTHONANYWHERE_SSH_KEY: [Your private SSH key]
     ```

### Step 2: PythonAnywhere Setup

1. **Sign up:** [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Create API token:** Account → API token → Create new token
3. **Generate SSH key:**
   ```bash
   ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f ~/.ssh/pythonanywhere_key
   ```
4. **Add SSH key to PythonAnywhere:**
   - Account → SSH keys → Add new key
   - Paste: `cat ~/.ssh/pythonanywhere_key.pub`

### Step 3: Supabase Setup

1. **Create project:** [supabase.com](https://supabase.com)
2. **Get credentials:** Settings → Database
3. **Update .env file** with your credentials

### Step 4: Deploy

1. **SSH into PythonAnywhere:**
   ```bash
   ssh bepratikshya@pythonanywhere.com
   ```

2. **Clone and setup:**
   ```bash
   git clone https://github.com/yourusername/health_bridge_hospital.git
   cd health_bridge_hospital/backend
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --user -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp env.example .env
   nano .env  # Update with your credentials
   ```

4. **Run initial setup:**
   ```bash
   python manage.py migrate --settings=healthbridge_backend.settings_production
   python manage.py createsuperuser --settings=healthbridge_backend.settings_production
   python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
   ```

5. **Configure web app in PythonAnywhere dashboard**

## 🔄 Automated Deployment

Once set up, every push to `main` will automatically deploy:

```bash
git add .
git commit -m "Update feature"
git push origin main
```

## 🛠️ Manual Deployment

```bash
# SSH into PythonAnywhere
ssh bepratikshya@pythonanywhere.com

# Deploy
cd /home/bepratikshya/health_bridge_hospital/backend
source venv/bin/activate
git pull origin main
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

2. **Database Connection Issues:**
   - Verify Supabase credentials in .env
   - Check database host and port

3. **Static Files Not Loading:**
   - Run: `python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production`

### Useful Commands:

```bash
# Check logs
tail -f /var/log/bepratikshya.pythonanywhere.com.error.log

# Test Django setup
python manage.py check --deploy --settings=healthbridge_backend.settings_production

# Check environment variables
python manage.py shell --settings=healthbridge_backend.settings_production -c "import os; print(os.environ.get('SECRET_KEY'))"
```

## 📊 Your Live API

After successful deployment:

- **Base URL:** `https://bepratikshya.pythonanywhere.com/api/`
- **Appointments:** `https://bepratikshya.pythonanywhere.com/api/appointments/`
- **Doctors:** `https://bepratikshya.pythonanywhere.com/api/doctors/`
- **Admin:** `https://bepratikshya.pythonanywhere.com/admin/`

## 🎯 Next Steps

1. **Update frontend** to use production API URL
2. **Set up monitoring** and alerts
3. **Configure backups** for your database
4. **Set up custom domain** (optional)

## 📞 Support

- **PythonAnywhere Help:** [help.pythonanywhere.com](https://help.pythonanywhere.com)
- **GitHub Actions:** [docs.github.com/actions](https://docs.github.com/en/actions)
- **Django Deployment:** [docs.djangoproject.com](https://docs.djangoproject.com/en/stable/howto/deployment/)

## 🎉 Success!

Your HealthBridge Hospital backend is now live on PythonAnywhere with automated deployment!

**Your API is available at:**
`https://bepratikshya.pythonanywhere.com/api/`

**Update your frontend to use this URL for production!**
