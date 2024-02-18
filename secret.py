import secrets
import hashlib

# Generate a secure random key
secret_key = secrets.token_hex(64)  # Generates a 64-character hexadecimal string (32 bytes)

# Hash the generated secret key with SHA-512
hashed_secret_key = hashlib.sha512(secret_key.encode()).hexdigest()

# Flask app configuration
SECRET_KEY = hashed_secret_key

