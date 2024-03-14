from fastapi import FastAPI
from src.database import engine, Base

from src.product_category.router import router as product_category_router
from src.manufacturer.router import router as manufacturer_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product_category_router)
app.include_router(manufacturer_router)