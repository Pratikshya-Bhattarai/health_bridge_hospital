# 🆓 Free Tier Deployment Instructions

## Quick Commands for PythonAnywhere Console

Copy and paste these commands one by one in your PythonAnywhere console:

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/health_bridge_hospital.git
cd health_bridge_hospital/backend
```

### 2. Set Up Virtual Environment
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install --user -r requirements.txt
```

### 3. Configure Environment
```bash
cp env.example .env
nano .env
```
*Edit the .env file with your credentials, then save (Ctrl+X, Y, Enter)*

### 4. Run Initial Setup
```bash
python manage.py migrate --settings=healthbridge_backend.settings_production
python manage.py createsuperuser --settings=healthbridge_backend.settings_production
python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
```

### 5. Update Your App (when you make changes)
```bash
cd /home/pratikshyabhattarai/health_bridge_hospital
git pull origin main
cd backend
source venv/bin/activate
pip install --user -r requirements.txt
python manage.py migrate --settings=healthbridge_backend.settings_production
python manage.py collectstatic --noinput --settings=healthbridge_backend.settings_production
```

## WSGI Configuration

In PythonAnywhere Web tab, set your WSGI file to:

```python
import os
import sys

path = '/home/pratikshyabhattarai/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

activate_this = '/home/pratikshyabhattarai/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Static Files Configuration

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/pratikshyabhattarai/health_bridge_hospital/backend/staticfiles` |
| `/media/` | `/home/pratikshyabhattarai/health_bridge_hospital/backend/media` |

## Your Live URLs

- **Site:** https://pratikshyabhattarai.pythonanywhere.com
- **API:** https://pratikshyabhattarai.pythonanywhere.com/api/
- **Admin:** https://pratikshyabhattarai.pythonanywhere.com/admin/
