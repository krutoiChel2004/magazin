from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB

from src.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name_product = Column(String, nullable=False, unique=True)
    description_product = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    discount_price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("product_category.id"))
    article_number = Column(Integer, nullable=False, unique=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturer.id"))
    characteristic = Column(JSONB, nullable=True)
    

