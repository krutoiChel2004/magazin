from fastapi import APIRouter, Depends, Response, Request
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

from starlette.status import HTTP_303_SEE_OTHER
from starlette.responses import RedirectResponse

from src.database import SessionLocal
from sqlalchemy.orm import Session

from src.auth.schemas import UserBase, Token, LoginData

from src.auth.service import (read_user_service, 
                              create_user_service, 
                              login_user_service)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
) 

@router.get("/{user_id}", response_model=UserBase)
async def read_user(user_id: int, db: db_dependency):
    return read_user_service(user_id, db)

@router.post("/create_user")
async def create_user(db: db_dependency,
                        user_data: UserBase):
    return create_user_service(user_data, db)

@router.post("/login", response_model=Token)
async def login_user(login_data: LoginData, db: db_dependency, response: Response):
    return login_user_service(login_data, db, response)

