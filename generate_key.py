from cryptography.fernet import Fernet

# Generate a secure encryption key
key = Fernet.generate_key()
print("\nSAVE THIS KEY:")
print(key.decode())
print("\nPut it inside your .env file like this:")
print(f"ENCRYPTION_KEY={key.decode()}\n")
