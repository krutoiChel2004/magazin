from sqlalchemy import Column, Integer, String

from src.database import Base

class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id = Column(Integer, primary_key=True, index=True)
    name_manufacturer = Column(String, nullable=False, unique=True)