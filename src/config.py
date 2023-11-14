import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PASS = os.environ.get("DB_PASS")
JWT_SECRET = os.environ.get("JWT_SECRET")

DB_PORT = 5432
DB_NAME = "postgres"
DB_USER = "postgres"
JWT_ALGORITHM = "HS256"
