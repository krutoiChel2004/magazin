from fastapi import APIRouter, Depends
from typing import Annotated

from src.database import get_db
from sqlalchemy.orm import Session

from src.product.scheme import (ProductBase,
                                DescriptionUpdateBase,
                                PriceUpdateBase,
                                DiscountPriceUpdateBase,
                                QtyUpdateBase,
                                CategoryUpdateBase,
                                ManufacturerUpdate,
                                CharacteristicsUpdate,
                                ListPathImageUpdate,
                                ArticleNumberUpdate,
                                NameProductUpdate)

from src.product.service import (create_product_service,
                                    get_product_service, 
                                    delete_product_service,
                                    update_product_description_service,
                                    update_product_price_service,
                                    update_product_discount_price_service,
                                    update_product_qty_service,
                                    update_product_category_service,
                                    update_product_manufacturer_service,
                                    update_product_characteristics_service,
                                    update_product_list_path_image_service,
                                    update_product_article_number_service,
                                    update_product_name_service)

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

@router.put("/update_product_name/{product_id}")
async def update_product_name(product_id: int, 
                              new_name: NameProductUpdate,
                              db: db_dependency):
    return update_product_name_service(product_id, new_name, db)

@router.put("/update_product_description/{product_id}")
async def update_product_description(product_id: int, 
                                        new_description: DescriptionUpdateBase,
                                        db: db_dependency):
    return update_product_description_service(product_id, new_description, db)

@router.put("/update_product_list_path_image/{product_id}")
async def update_product_list_path_image(product_id: int, 
                                         new_list_path_image: ListPathImageUpdate,
                                         db: db_dependency):
    return update_product_list_path_image_service(product_id, new_list_path_image, db)

@router.put("/update_product_price/{product_id}")
async def update_product_price(product_id: int, 
                                new_price: PriceUpdateBase,
                                db: db_dependency):
    return update_product_price_service(product_id, new_price, db)

@router.put("/update_product_discount_price/{product_id}")
async def update_product_discount_price(product_id: int, 
                                        new_discount_price: DiscountPriceUpdateBase,
                                        db: db_dependency):
    return update_product_discount_price_service(product_id, new_discount_price, db)

@router.put("/update_product_qty/{product_id}")
async def update_product_qty(product_id: int, 
                             new_qty: QtyUpdateBase,
                             db: db_dependency):
    return update_product_qty_service(product_id, new_qty, db)

@router.put("/update_product_category/{product_id}")
async def update_product_category(product_id: int, 
                                  new_category_id: CategoryUpdateBase,
                                  db: db_dependency):
    return update_product_category_service(product_id, new_category_id, db)

@router.put("/update_product_article_number/{product_id}")
async def update_product_article_number(product_id: int, 
                                        new_article_number: ArticleNumberUpdate,
                                        db: db_dependency):
    return update_product_article_number_service(product_id, new_article_number, db)

@router.put("/update_product_manufacturer/{product_id}")
async def update_product_manufacturer(product_id: int, 
                                      new_manufacturer_id: ManufacturerUpdate,
                                      db: db_dependency):
    return update_product_manufacturer_service(product_id, new_manufacturer_id, db)

@router.put("/update_product_characteristics/{product_id}")
async def update_product_characteristics(product_id: int, 
                                         new_characteristics: CharacteristicsUpdate,
                                         db: db_dependency):
    return update_product_characteristics_service(product_id, new_characteristics, db)





