import os
from dotenv import load_dotenv

load_dotenv()

# --- База данных ---
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_NAME = os.environ['DB_NAME']

# --- Секретный ключ ---
SECRET_KEY = os.environ['SECRET_KEY']
