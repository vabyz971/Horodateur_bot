import sqlite3
from contextlib import contextmanager
from config import Config
import logging


class DatabaseManager:
    def __init__(self):
        self.connect = None

    @contextmanager
    def get_connection(self):
        """Gestion contextuelle des connexions"""
        try:
            self.connect = sqlite3.connect(Config.DB_PATH)
            self.connect.row_factory = sqlite3.Row
            yield self.connect
        finally:
            if self.connect:
                self.connect.close()

    def initialize_database(self):
        """Initialisation de la base de données"""
        logging.info("Initialisation de la base de données...")
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # Création des tables
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users  
                ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_slack VARCHAR UNIQUE NOT NULL, 
                name VARCHAR NOT NULL,
                groupe VARCHAR NOT NULL 
                )"""
            )
            conn.commit()


# Singleton pour la connexion DB
db_manager = DatabaseManager()
