from sqlalchemy import Column, Integer, String

from src.database import Base

class ProductCategory(Base):
    __tablename__ = "product_category"

    id = Column(Integer, primary_key=True, index=True)
    name_category = Column(String, nullable=False, unique=True)