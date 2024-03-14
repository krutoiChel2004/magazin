from pydantic import BaseModel
from typing import Dict

class ProductBase(BaseModel):
    name_product: str
    description_product: str
    price: int
    discount_price: int
    category_id: int
    article_number: int
    manufacturer_id: int
    characteristics: Dict[str, str] = {}