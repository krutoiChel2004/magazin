from fastapi import HTTPException, Depends, Response, Request
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from starlette import status
from datetime import timedelta, datetime
from jose import jwt, JWTError

from starlette.status import HTTP_303_SEE_OTHER
from starlette.responses import RedirectResponse

from sqlalchemy.orm import Session

from src.cart.service import create_cart_service

from src.auth.schemas import (UserBase, 
                              Token, 
                              LoginData)

from src.auth.models import User

from src.config import SECRET_KEY, ALGORITHM


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def read_user_service(user_id: int, db: Session):
    task = db.query(User).filter(User.id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="User not found")
    return task


def create_user_service(user: UserBase, db: Session):
    db_user = User(mail=user.mail,
                    hashed_password=bcrypt_context.hash(user.hashed_password),
                    countr_code=user.countr_code,
                    phone=user.phone,
                    name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    user = db.query(User).filter(User.mail==user.mail).first()

    create_cart_service(db, user.id)

    


def login_user_service(login_data: LoginData,
                     db: Session,
                     response: Response):
    user = auth_user(login_data.mail, login_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')

    token = create_access_token(user.mail, user.id, timedelta(minutes=1000))

    response.set_cookie(key="access_token", value=token, httponly=True)
    
    return {"access_token": token, "token_type": "bearer"}
    

def auth_user(mail: str, password: str, db: Session):
    user = db.query(User).filter(User.mail == mail).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(mail: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': mail, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')


