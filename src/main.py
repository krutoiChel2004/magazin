from fastapi import FastAPI, Cookie, Depends
from typing import Annotated

from src.database import engine, Base
from src.database import get_db
from sqlalchemy.orm import Session

from src.product_category.router import router as product_category_router
from src.manufacturer.router import router as manufacturer_router
from src.product.router import router as product_router
from src.auth.router import router as auth_router
from src.client.client import router as client_router
from src.cart.router import router as cart_router

db_dependency = Annotated[Session, Depends(get_db)]

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product_category_router)
app.include_router(manufacturer_router)
app.include_router(product_router)
app.include_router(auth_router)
app.include_router(client_router)
app.include_router(cart_router)