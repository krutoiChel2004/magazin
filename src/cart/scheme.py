from pydantic import BaseModel

class ItemCartBase(BaseModel):
    product_id: int
    qty: int

class CartBase(BaseModel):
    user_id: int