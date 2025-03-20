from sqlalchemy import create_engine
from config import Config


def start_engine():
    return create_engine(f"sqlite:///{Config.DB_PATH}", echo = True)