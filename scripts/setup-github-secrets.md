# 🔐 GitHub Secrets Setup for PythonAnywhere Deployment

## Overview

This guide explains how to set up GitHub secrets for automated deployment to PythonAnywhere.

## Required Secrets

You need to add the following secrets to your GitHub repository:

### 1. PYTHONANYWHERE_HOST
- **Value:** `pythonanywhere.com`
- **Description:** The hostname for PythonAnywhere SSH connection

### 2. PYTHONANYWHERE_USERNAME
- **Value:** `bepratikshya`
- **Description:** Your PythonAnywhere username

### 3. PYTHONANYWHERE_SSH_KEY
- **Value:** Your SSH private key content
- **Description:** Private SSH key for authenticating with PythonAnywhere

## Step-by-Step Setup

### Step 1: Generate SSH Key Pair

If you don't have an SSH key pair, generate one:

```bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "bepratikshya@gmail.com" -f ~/.ssh/pythonanywhere_key

# This creates:
# - ~/.ssh/pythonanywhere_key (private key)
# - ~/.ssh/pythonanywhere_key.pub (public key)
```

### Step 2: Add Public Key to PythonAnywhere

1. **Copy your public key:**
   ```bash
   cat ~/.ssh/pythonanywhere_key.pub
   ```

2. **Log in to PythonAnywhere:**
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Username: `bepratikshya`
   - Password: `rxcqm%pD995B6p+`

3. **Add SSH key:**
   - Go to **Account** tab
   - Scroll down to **SSH keys**
   - Click **Add a new key**
   - Paste your public key
   - Click **Add key**

### Step 3: Add Secrets to GitHub

1. **Go to your GitHub repository**
2. **Click Settings** (in the repository, not your account)
3. **Click Secrets and variables** → **Actions**
4. **Click New repository secret**

#### Add PYTHONANYWHERE_HOST:
- **Name:** `PYTHONANYWHERE_HOST`
- **Secret:** `pythonanywhere.com`

#### Add PYTHONANYWHERE_USERNAME:
- **Name:** `PYTHONANYWHERE_USERNAME`
- **Secret:** `bepratikshya`

#### Add PYTHONANYWHERE_SSH_KEY:
- **Name:** `PYTHONANYWHERE_SSH_KEY`
- **Secret:** Copy the entire content of your private key file:
  ```bash
  cat ~/.ssh/pythonanywhere_key
  ```
  Copy everything including the `-----BEGIN OPENSSH PRIVATE KEY-----` and `-----END OPENSSH PRIVATE KEY-----` lines.

### Step 4: Test SSH Connection

Test that your SSH key works:

```bash
# Test SSH connection to PythonAnywhere
ssh bepratikshya@pythonanywhere.com

# You should see a welcome message and be logged in
# Type 'exit' to disconnect
```

### Step 5: Test GitHub Actions

1. **Push a change to your repository:**
   ```bash
   git add .
   git commit -m "Test automated deployment"
   git push origin main
   ```

2. **Check GitHub Actions:**
   - Go to your repository on GitHub
   - Click **Actions** tab
   - You should see the deployment workflow running
   - Click on it to see the logs

## Troubleshooting

### SSH Connection Issues

If SSH connection fails:

1. **Check SSH key format:**
   ```bash
   # Make sure the key is in OpenSSH format
   head -1 ~/.ssh/pythonanywhere_key
   # Should show: -----BEGIN OPENSSH PRIVATE KEY-----
   ```

2. **Check file permissions:**
   ```bash
   chmod 600 ~/.ssh/pythonanywhere_key
   chmod 644 ~/.ssh/pythonanywhere_key.pub
   ```

3. **Test SSH connection:**
   ```bash
   ssh -v bepratikshya@pythonanywhere.com
   ```

### GitHub Actions Issues

If GitHub Actions fails:

1. **Check secrets are correctly set:**
   - Go to repository → Settings → Secrets and variables → Actions
   - Verify all three secrets are present

2. **Check SSH key format:**
   - Make sure the private key includes the header and footer lines
   - No extra spaces or characters

3. **Check PythonAnywhere SSH access:**
   - Log in to PythonAnywhere
   - Go to Account tab
   - Verify SSH key is added and enabled

### Common Error Messages

#### "Permission denied (publickey)"
- SSH key not added to PythonAnywhere
- Wrong username in secrets
- SSH key format incorrect

#### "Host key verification failed"
- Add PythonAnywhere to known hosts:
  ```bash
  ssh-keyscan pythonanywhere.com >> ~/.ssh/known_hosts
  ```

#### "No such file or directory"
- Check file paths in the workflow
- Verify the project structure on PythonAnywhere

## Security Best Practices

1. **Never commit SSH keys to your repository**
2. **Use environment-specific keys**
3. **Rotate keys regularly**
4. **Use least privilege principle**
5. **Monitor access logs**

## Alternative: Using SSH Agent

If you prefer using SSH agent:

```bash
# Start SSH agent
eval "$(ssh-agent -s)"

# Add your key
ssh-add ~/.ssh/pythonanywhere_key

# Test connection
ssh bepratikshya@pythonanywhere.com
```

## Verification Checklist

- [ ] SSH key pair generated
- [ ] Public key added to PythonAnywhere
- [ ] Private key added to GitHub secrets
- [ ] SSH connection tested
- [ ] GitHub Actions workflow created
- [ ] First deployment successful

## Support

If you encounter issues:

1. **Check GitHub Actions logs** for detailed error messages
2. **Test SSH connection manually** to isolate issues
3. **Verify all secrets are correctly set**
4. **Check PythonAnywhere account status**

---

## 🎉 Success!

Once all secrets are configured, your repository will automatically deploy to PythonAnywhere whenever you push to the main branch!
