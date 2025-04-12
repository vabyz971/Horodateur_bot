import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATABASE_NAME = f"{os.getenv('DATABASE_NAME')}.db"

class Config:
    DB_PATH = str(BASE_DIR / DATABASE_NAME)