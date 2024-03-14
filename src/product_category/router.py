from fastapi import APIRouter, Depends
from typing import Annotated

from src.database import get_db
from sqlalchemy.orm import Session

from src.product_category.scheme import ProductCategoryBase
from src.product_category.model import ProductCategory

from src.product_category.service import (create_product_category_service,
                                          get_product_category_service,
                                          delete_product_category_service)

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/product_category",
    tags=["product_category"],
    # responses={404: {"description": "Not found"}},
)

@router.post("/create_product_category")
async def create_product_category(db: db_dependency, product_category: ProductCategoryBase):
    create_product_category_service(db, product_category)
    return product_category

@router.get("/get_product_category")
async def get_product_category(db: db_dependency):
    return get_product_category_service(db)

@router.delete("/delete_product_category/{category_id}")
async def delete_product_category(category_id: int, 
                                  db: db_dependency):
    return delete_product_category_service(category_id, db)