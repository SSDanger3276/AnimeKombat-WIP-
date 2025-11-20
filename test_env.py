from dotenv import load_dotenv
import os

# Load everything from the .env file
load_dotenv()

key = os.getenv("ENCRYPTION_KEY")

print("Loaded Key:", key)
