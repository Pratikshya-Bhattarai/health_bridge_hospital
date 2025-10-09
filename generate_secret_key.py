import secrets
import string

def generate_secret_key():
    chars = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(chars) for _ in range(50))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(f"SECRET_KEY = {secret_key}")
