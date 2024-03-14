from sqlalchemy import Column, Integer, String, ForeignKey

from src.database import Base

class ProductCategory(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name_product = Column(String, nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    discount_price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("product_category.id"))
    article_number = Column(Integer, nullable=False, unique=True)
    

