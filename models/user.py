from database.database import db_manager

class User:
    def __init__(self, user_id: str, name: str, groupe : str):
        self.id = user_id
        self.name = name
        self.groupe = groupe

    @classmethod
    def get_by_id(cls, user_id):
        """Récupère un utilisateur par son ID"""
        with db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id_slack = ?", (user_id,))
            result = cursor.fetchone()
            return cls(**result) if result else None

    def get_all():
        """Récupère tous les utilisateurs"""
        with db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchone()
            print(dict(result))
            return result

    def save(self):
        """Sauvegarde l'utilisateur en base"""
        with db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO users (id_slack, name, groupe)
                VALUES (?, ?, ?)
            """,
                (self.id, self.name, self.groupe),
            )
            conn.commit()
            return True
