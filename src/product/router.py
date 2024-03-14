from fastapi import APIRouter, Depends
from typing import Annotated

from src.database import get_db
from sqlalchemy.orm import Session

from src.product.scheme import ProductBase

from src.product.service import (create_product_service,
                                    get_product_service, 
                                    delete_product_service)

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

@router.post("/create_product")
async def create_product(db: db_dependency, product: ProductBase):
    create_product_service(db, product)
    return product

@router.get("/get_product")
async def get_product(db: db_dependency):
    return get_product_service(db)

@router.delete("/delete_product/{product_id}")
async def delete_product(product_id: int, 
                         db: db_dependency):
    return delete_product_service(product_id, db)