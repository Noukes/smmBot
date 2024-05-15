from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from data.models.base import Base


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def init(self, path: str):
        self.engine = create_engine(path, echo=True)
        Base.metadata.create_all(bind=self.engine)
