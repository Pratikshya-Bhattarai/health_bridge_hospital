"""
WSGI configuration for PythonAnywhere deployment
Copy this content to your WSGI file in PythonAnywhere
"""

import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/health_bridge_hospital/backend'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthbridge_backend.settings_production'

# Activate virtual environment
activate_this = '/home/yourusername/health_bridge_hospital/backend/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
