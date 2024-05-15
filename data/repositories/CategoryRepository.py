from sqlalchemy.orm import Session
from data.database import Database
from data.models.category import Category


class CategoryRepository:

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CategoryRepository, cls).__new__(cls)
        return cls._instance

    async def add(name: str):
        with Session(autoflush=False, bind=Database().engine) as db:
            category = Category(name=name)
            db.add(category)
            await db.commit()

    async def get_by_id(id: int):
        with Session(autoflush=False, bind=Database().engine) as db:
            return await db.get(Category, id)

    async def get_all(id: int):
        with Session(autoflush=False, bind=Database().engine) as db:
            return await db.query(Category).all()

    async def delete(category: Category):
        with Session(autoflush=False, bind=Database().engine) as db:
            db.delete(category)
            await db.commit()
