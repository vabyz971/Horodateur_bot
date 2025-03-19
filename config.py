import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_NAME = f"{os.getenv('DATABASE_NAME')}.db"

class Config:
    DB_PATH = str(BASE_DIR / DATABASE_NAME)