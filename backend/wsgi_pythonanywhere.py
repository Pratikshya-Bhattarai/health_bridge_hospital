"""
WSGI configuration for HealthBridge Hospital on PythonAnywhere.
This file should be placed at: /var/www/pratikshyabhattarai_pythonanywhere_com_wsgi.py
"""

import os
import sys

# Add the project directory to Python path
path = '/home/pratikshyabhattarai/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

# Activate virtual environment
activate_this = '/home/pratikshyabhattarai/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()