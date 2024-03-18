from fastapi import APIRouter, Depends
from typing import Annotated

from src.database import get_db
from sqlalchemy.orm import Session

from src.client.client import get_user_JWT
from src.cart.service import (create_cart_service,
                                       add_item_cart_service,
                                       get_cart_service,
                                       add_quantity_item_cart_service,
                                       reduce_quantity_item_cart_service,
                                       check_product_in_cart,
                                       check_cart_service)

from src.cart.scheme import CartBase
from src.cart.scheme import ItemCartBase
from src.cart.model import ItemCart




db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/cart",
    tags=["Cart"],
    # responses={404: {"description": "Not found"}},
)


# @router.post("/create_cart")
# async def create_cart(db: db_dependency, 
#                       user_JWT: dict = Depends(get_user_JWT)):
#     return create_cart_service(db, user_JWT)

@router.post("/add_item_cart")
async def add_item_cart(item_cart: ItemCartBase, 
                        db: db_dependency, 
                        user_JWT: dict = Depends(get_user_JWT)):
    return add_item_cart_service(item_cart, db, user_JWT)

@router.get("/get_cart")
async def get_cart(db: db_dependency, 
                   user_JWT: dict = Depends(get_user_JWT)):
    return get_cart_service(db, user_JWT)

@router.put("/reduce_quantity_item_cart/{product_id}")
async def reduce_quantity_item_cart(db: db_dependency,
                                    product_id: int,
                                    qty: int = 1,
                                    user_JWT: dict = Depends(get_user_JWT)):
    user_id = user_JWT.get("id")
    cart_id = check_cart_service(db, user_id).id
    item = check_product_in_cart(db, cart_id, product_id)
    return reduce_quantity_item_cart_service(item, db, qty)

@router.put("/add_quantity_item_cart/{product_id}")
async def add_quantity_item_cart(db: db_dependency,
                                    product_id: int,
                                    qty: int = 1,
                                    user_JWT: dict = Depends(get_user_JWT)):
    user_id = user_JWT.get("id")
    cart_id = check_cart_service(db, user_id).id
    item = check_product_in_cart(db, cart_id, product_id)
    return add_quantity_item_cart_service(item, db, qty)
    