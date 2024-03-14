from fastapi import APIRouter, Depends
from typing import Annotated

from src.database import get_db
from sqlalchemy.orm import Session

from src.manufacturer.scheme import ManufacturerBase

from src.manufacturer.service import (create_manufacturer_service,
                                        get_manufacturer_service,
                                        delete_manufacturer_service)

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/manufacturer",
    tags=["manufacturer"],
)

@router.post("/create_manufacturer")
async def create_manufacturer(db: db_dependency, product_category: ManufacturerBase):
    create_manufacturer_service(db, product_category)
    return product_category

@router.get("/get_manufacturer")
async def get_manufacturer(db: db_dependency):
    return get_manufacturer_service(db)

@router.delete("/delete_manufacturer/{manufacturer_id}")
async def delete_manufacturer(manufacturer_id: int, 
                                  db: db_dependency):
    return delete_manufacturer_service(manufacturer_id, db)