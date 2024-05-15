from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data.models.base import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    name = Column(String, nullable=False, unique=True)
    subcategories = relationship("Subcategory", back_populates="subcategory")
