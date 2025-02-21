import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'database': os.getenv('DB_NAME'),
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}