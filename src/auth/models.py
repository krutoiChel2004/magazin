from sqlalchemy import Column, Integer, String, DateTime
import pytz 
from datetime import datetime
from src.database import Base

def get_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    mail = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    countr_code = Column(String(3), nullable=False)
    phone = Column(String(10), unique=True)
    name = Column(String, nullable=False)
    date_create = Column(DateTime, nullable=False, default=get_time)