from pydantic import BaseModel

class ProductCategoryBase(BaseModel):
    name_category: str