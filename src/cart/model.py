from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB

from src.database import Base

class ItemCart(Base):
    __tablename__ = "item_cart"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    qty = Column(Integer, nullable=False)
    cart_id = Column(Integer, ForeignKey("cart.id"), nullable=False)

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, unique=True)
    