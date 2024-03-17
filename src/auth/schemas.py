from pydantic import BaseModel
from enum import Enum

class CountryCode(str, Enum):
    RU = "7"
    KZ = "7"
    BY = "375"


class LoginData(BaseModel):
    mail: str
    password: str

class UserBase(BaseModel):
    mail: str
    hashed_password: str
    countr_code: CountryCode
    phone: str
    name: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
