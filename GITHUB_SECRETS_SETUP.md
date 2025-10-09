# 🔐 GitHub Secrets Setup Guide

## Required Secrets for Deployment

Add these secrets to your GitHub repository at:
**Settings → Secrets and variables → Actions → New repository secret**

### 1. PythonAnywhere Secrets
```
PYTHONANYWHERE_API_TOKEN = [Your PythonAnywhere API Token]
PYTHONANYWHERE_USERNAME = [Your PythonAnywhere Username]
```

### 2. Database Secrets (Supabase)
```
DB_NAME = postgres
DB_USER = postgres
DB_PASSWORD = [Your Supabase Database Password]
DB_HOST = [Your Supabase Database Host - looks like db.xxxxxxxxxxxxx.supabase.co]
DB_PORT = 5432
```

### 3. Django Secret Key
```
SECRET_KEY = djangosecretkey2024!@#$%^&*(-_=+)abcdefghijklmnopqrstuvwxyz0123456789
```

## How to Add Secrets:

1. Go to: https://github.com/Pratikshya-Bhattarai/health_bridge_hospital/settings/secrets/actions
2. Click "New repository secret"
3. Enter the name (e.g., `PYTHONANYWHERE_API_TOKEN`)
4. Enter the value
5. Click "Add secret"
6. Repeat for all secrets above

## Example Secret Values:

- **PYTHONANYWHERE_API_TOKEN**: `abc123def456ghi789` (from PythonAnywhere)
- **PYTHONANYWHERE_USERNAME**: `bepratikshya` (your PythonAnywhere username)
- **DB_PASSWORD**: `your_supabase_password` (from Supabase)
- **DB_HOST**: `db.abcdefghijklmnop.supabase.co` (from Supabase)
- **SECRET_KEY**: `djangosecretkey2024!@#$%^&*(-_=+)abcdefghijklmnopqrstuvwxyz0123456789`

## After Adding All Secrets:

1. Go to the Actions tab in your GitHub repository
2. You should see the deployment workflow
3. Click on it to monitor the deployment process
