from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB

from src.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name_product = Column(String, nullable=False, unique=True)
    description_product = Column(String, nullable=True)
    list_path_image = Column(ARRAY(String), nullable=True)
    price = Column(Integer, nullable=False)
    discount_price = Column(Integer, nullable=True)
    qty = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("product_category.id"), nullable=False)
    article_number = Column(String, nullable=False, unique=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturer.id"), nullable=False)
    characteristics = Column(JSONB, nullable=True)
    

