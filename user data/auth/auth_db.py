import sqlite3
import bcrypt
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load env
load_dotenv()
KEY = os.getenv("ENCRYPTION_KEY")
fernet = Fernet(KEY)

DB_NAME = "users.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


# -------- PASSWORDS --------
def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(password: str, stored_hash: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), stored_hash)


# -------- EMAIL --------
def encrypt_email(email: str) -> bytes:
    return fernet.encrypt(email.encode())


def decrypt_email(encrypted_email: bytes) -> str:
    return fernet.decrypt(encrypted_email).decode()


# -------- AUTH --------
def sign_up(username, password, email):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (username, password, email)
            VALUES (?, ?, ?)
            """,
            (
                username,
                hash_password(password),
                encrypt_email(email)
            )
        )
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def log_in(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        return False

    return check_password(password, row[0])
