from pydantic import BaseModel
from typing import Dict

class ProductBase(BaseModel):
    name_product: str
    description_product: str
    list_path_image: list[str]
    price: int
    discount_price: int
    qty: int
    category_id: int
    article_number: str
    manufacturer_id: int
    characteristics: Dict[str, str] = {}

class NameProductUpdate(BaseModel):
    name_product: str

class DescriptionUpdateBase(BaseModel):
    description: str

class PriceUpdateBase(BaseModel):
    price: int

class DiscountPriceUpdateBase(BaseModel):
    discount_price: int

class QtyUpdateBase(BaseModel):
    qty: int

class CategoryUpdateBase(BaseModel):
    category_id: int

class ManufacturerUpdate(BaseModel):
    manufacturer_id: int

class CharacteristicsUpdate(BaseModel):
    characteristics: Dict[str, str]

class ListPathImageUpdate(BaseModel):
    list_path_image: list[str]

class ArticleNumberUpdate(BaseModel):
    article_number: str



