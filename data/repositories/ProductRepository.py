from sqlalchemy.orm import Session
from data.database import Database
from data.models.category import Category
from data.models.product import Product
from data.models.subcategory import Subcategory


class SubcategoryRepository:

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SubcategoryRepository, cls).__new__(cls)
        return cls._instance

    async def add(name: str, cost: int, subcategory: Subcategory):
        with Session(autoflush=False, bind=Database().engine) as db:
            product = Product(name=name, cost=cost, subcategory=subcategory)
            db.add(subcategory)
            await db.commit()

    async def get_by_id(id: int):
        with Session(autoflush=False, bind=Database().engine) as db:
            return await db.get(Product, id)

    async def get_all(id: int):
        with Session(autoflush=False, bind=Database().engine) as db:
            return await db.query(Product).all()

    async def delete(product: Product):
        with Session(autoflush=False, bind=Database().engine) as db:
            db.delete(product)
            await db.commit()
