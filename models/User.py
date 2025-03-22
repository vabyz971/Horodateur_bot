from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Sequence, String
from database import EngineDatabase


engine = EngineDatabase.start_engine()

class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key = True)
    id_slack = Column(String(50), nullable=False , unique = True)
    name = Column(String(50), nullable=False)
    groupe = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f"User (id={self.id!r}, id_slack={self.id_slack!r}, name={self.name!r}, groupe={self.groupe!r})"


Base.metadata.create_all(engine)