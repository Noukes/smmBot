from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data.models.base import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    name = Column(String, nullable=False, unique=True)
    cost = Column(Integer, nullable=False)
    subcategory = relationship("Subcategory", back_populates="subcategory")