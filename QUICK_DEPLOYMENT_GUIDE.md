# 🚀 Quick Deployment Guide - HealthBridge Hospital

## 📋 Overview

This guide provides a quick setup for deploying HealthBridge Hospital to PythonAnywhere with automated GitHub deployment.

## 🔐 Your Credentials

- **PythonAnywhere Username:** `bepratikshya`
- **PythonAnywhere Password:** `rxcqm%pD995B6p+`
- **Email:** `bepratikshya@gmail.com`

## ⚡ Quick Start (5 Minutes)

### Step 1: Set Up GitHub Secrets

1. **Go to your GitHub repository**
2. **Settings** → **Secrets and variables** → **Actions**
3. **Add these secrets:**

```
PYTHONANYWHERE_HOST: pythonanywhere.com
PYTHONANYWHERE_USERNAME: bepratikshya
PYTHONANYWHERE_SSH_KEY: [Your SSH private key - see below]
```

### Step 2: Generate SSH Key

```bash
# Generate SSH key
ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f ~/.ssh/pythonanywhere_key

# Copy public key
cat ~/.ssh/pythonanywhere_key.pub
```

### Step 3: Add SSH Key to PythonAnywhere

1. **Log in to PythonAnywhere:** [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Account tab** → **SSH keys**
3. **Add new key** → Paste your public key
4. **Enable SSH access**

### Step 4: Add Private Key to GitHub

1. **Copy your private key:**
   ```bash
   cat ~/.ssh/pythonanywhere_key
   ```

2. **Add to GitHub secrets:**
   - Name: `PYTHONANYWHERE_SSH_KEY`
   - Value: Paste the entire private key content

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
   
   **Update .env with your Supabase credentials:**
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=bepratikshya.pythonanywhere.com,www.bepratikshya.pythonanywhere.com
   DB_NAME=your-supabase-db-name
   DB_USER=your-supabase-user
   DB_PASSWORD=your-supabase-password
   DB_HOST=db.your-project.supabase.co
   DB_PORT=5432
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-supabase-anon-key
   ```

5. **Run initial setup:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic --noinput
   ```

### Step 6: Configure Web App

1. **Go to PythonAnywhere Web tab**
2. **Add a new web app** → **Manual Configuration** → **Python 3.10**
3. **Configure WSGI file:**

   **File:** `/var/www/bepratikshya_pythonanywhere_com_wsgi.py`
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

### Step 7: Test Deployment

1. **Visit your site:** `https://bepratikshya.pythonanywhere.com`
2. **Test API:** `https://bepratikshya.pythonanywhere.com/api/`
3. **Check admin:** `https://bepratikshya.pythonanywhere.com/admin/`

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
python manage.py migrate
python manage.py collectstatic --noinput
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

4. **Static Files Not Loading:**
   - Run: `python manage.py collectstatic --noinput`
   - Check static file mappings in PythonAnywhere Web tab

### Useful Commands:

```bash
# Check logs
tail -f /var/log/bepratikshya.pythonanywhere.com.error.log

# Check Django logs
tail -f /home/bepratikshya/health_bridge_hospital/backend/logs/django.log

# Test Django setup
python manage.py check --deploy

# Check environment variables
python manage.py shell -c "import os; print(os.environ.get('SECRET_KEY'))"
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

---

## 🎉 Success!

Your HealthBridge Hospital backend is now live on PythonAnywhere with automated deployment!

**Your API is available at:**
`https://bepratikshya.pythonanywhere.com/api/`

**Update your frontend to use this URL for production!**
