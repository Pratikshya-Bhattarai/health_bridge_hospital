# 🚀 PythonAnywhere Quick Reference

## 📋 Pre-Deployment Checklist

### ✅ Files Ready:
- `backend/` folder with Django project
- `requirements.txt` (production requirements)
- `settings_production.py` (production settings)
- `.env` file with Supabase credentials

### 🔐 Environment Variables Needed:
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DB_NAME=your-supabase-db-name
DB_USER=your-supabase-user
DB_PASSWORD=your-supabase-password
DB_HOST=your-supabase-host
DB_PORT=5432
```

## 🚀 Deployment Steps

### 1. Create PythonAnywhere Account
- Go to [pythonanywhere.com](https://www.pythonanywhere.com)
- Sign up for free account
- Verify email

### 2. Upload Your Code
**Option A: Git Clone (Recommended)**
```bash
git clone https://github.com/yourusername/health_bridge_hospital.git
cd health_bridge_hospital/backend
```

**Option B: Direct Upload**
- Upload `backend/` folder via Files tab
- Extract and organize files

### 3. Set Up Virtual Environment
```bash
# Navigate to project
cd /home/yourusername/health_bridge_hospital/backend

# Create virtual environment
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install --user -r requirements.txt
```

### 4. Configure Database
```bash
# Create .env file with your Supabase credentials
nano .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 5. Configure Web App
1. **Go to Web tab** in PythonAnywhere dashboard
2. **Click "Add a new web app"**
3. **Choose "Manual Configuration"**
4. **Select Python 3.10**
5. **Configure paths:**
   - Source code: `/home/yourusername/health_bridge_hospital/backend`
   - Working directory: `/home/yourusername/health_bridge_hospital/backend`

### 6. WSGI Configuration
**File:** `/var/www/yourusername_pythonanywhere_com_wsgi.py`

```python
import os
import sys

path = '/home/yourusername/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

activate_this = '/home/yourusername/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 7. Static Files Configuration
- **URL:** `/static/`
- **Directory:** `/home/yourusername/health_bridge_hospital/backend/staticfiles`

### 8. Test Your Deployment
1. **Reload web app** (green reload button)
2. **Visit:** `https://yourusername.pythonanywhere.com`
3. **Test API:** `https://yourusername.pythonanywhere.com/api/appointments/`

## 🔧 Troubleshooting

### Common Issues:
- **Import errors:** Check virtual environment activation
- **Database errors:** Verify Supabase credentials
- **Static files:** Run `collectstatic` command
- **CORS issues:** Update `CORS_ALLOWED_ORIGINS` in settings

### Useful Commands:
```bash
# Check logs
tail -f /var/log/yourusername.pythonanywhere.com.error.log

# Restart web app
# Go to Web tab → Reload

# Check Django logs
tail -f /home/yourusername/health_bridge_hospital/backend/logs/django.log
```

## 📊 Your Live API Endpoints

After successful deployment, your API will be available at:

- **Base URL:** `https://yourusername.pythonanywhere.com/api/`
- **Appointments:** `https://yourusername.pythonanywhere.com/api/appointments/`
- **Doctors:** `https://yourusername.pythonanywhere.com/api/doctors/`
- **Services:** `https://yourusername.pythonanywhere.com/api/services/`
- **API Docs:** `https://yourusername.pythonanywhere.com/api/docs/`

## 🔄 Update Frontend

Once your backend is live, update your frontend API configuration:

```typescript
// lib/api.ts
const API_BASE_URL = 'https://yourusername.pythonanywhere.com/api'
```

## 🎉 Success!

Your Django backend is now live on PythonAnywhere! 

**Next steps:**
1. Test all API endpoints
2. Update frontend to use production API
3. Set up monitoring and backups
4. Configure custom domain (optional)

---

**📖 Full Guide:** `PYTHONANYWHERE_DEPLOYMENT_GUIDE.md`
