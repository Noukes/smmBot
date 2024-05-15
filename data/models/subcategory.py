from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data.models.base import Base


class Subcategory(Base):
    __tablename__ = "subcategory"

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    name = Column(String, nullable=False, unique=True)
    subcategory = relationship("Category", back_populates="category")
    products = relationship("Product", back_populates="product")
