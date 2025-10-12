# 🔐 GitHub Secrets Setup Guide

## 🚨 Fix GitHub Actions Failures

Your GitHub Actions are failing because the required secrets are not configured. Here's how to fix them:

### For PythonAnywhere Deployment (Backend)

You need to set up these secrets in your GitHub repository:

1. **Go to your GitHub repository**
2. **Click on "Settings" tab**
3. **Click on "Secrets and variables" → "Actions"**
4. **Click "New repository secret"**

Add these secrets:

#### Required Secrets for PythonAnywhere:

| Secret Name | Description | How to Get |
|-------------|-------------|------------|
| `PYTHONANYWHERE_HOST` | Your PythonAnywhere SSH host | From PythonAnywhere account settings |
| `PYTHONANYWHERE_USERNAME` | Your PythonAnywhere username | Your PythonAnywhere username |
| `PYTHONANYWHERE_SSH_KEY` | Your SSH private key | Generate SSH key pair |

### For Vercel Deployment (Frontend)

Add these secrets for Vercel:

| Secret Name | Description | How to Get |
|-------------|-------------|------------|
| `VERCEL_TOKEN` | Your Vercel API token | From Vercel dashboard → Settings → Tokens |
| `VERCEL_ORG_ID` | Your Vercel organization ID | From Vercel dashboard → Settings → General |
| `VERCEL_PROJECT_ID` | Your Vercel project ID | From Vercel project settings |

## 🔧 How to Get PythonAnywhere SSH Access

### Option 1: Free Tier (No SSH)
- The workflow will skip automatically if no SSH secrets are provided
- Use manual deployment instead

### Option 2: Paid Tier (With SSH)
1. **Upgrade to PythonAnywhere paid plan**
2. **Enable SSH access**
3. **Generate SSH key pair:**
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
   ```
4. **Add public key to PythonAnywhere:**
   - Go to PythonAnywhere → Account → SSH keys
   - Add your public key
5. **Add private key to GitHub secrets**

## 🚀 Quick Fix (Skip SSH for Now)

If you don't have SSH access, the workflow will automatically skip the PythonAnywhere deployment step. This is fine for now.

### To disable the workflow temporarily:

1. **Go to your repository**
2. **Click on "Actions" tab**
3. **Click on "Deploy Backend to PythonAnywhere"**
4. **Click on the three dots → "Disable workflow"**

## 📋 Current Status

After setting up the secrets:
- ✅ PythonAnywhere deployment will work (if you have SSH access)
- ✅ Vercel deployment will work (if you have Vercel account)
- ✅ Workflows will only run when secrets are available

## 🎯 Next Steps

1. **Set up the required secrets** (if you have the accounts)
2. **Or disable the workflows** temporarily
3. **Use manual deployment** for PythonAnywhere (free tier)
4. **Test your deployments** once secrets are configured

## 💡 Alternative: Manual Deployment

If you don't want to set up SSH, you can:
1. **Disable the GitHub workflow**
2. **Use manual deployment** following the PythonAnywhere setup guide
3. **Deploy frontend to Vercel** manually or through Vercel dashboard