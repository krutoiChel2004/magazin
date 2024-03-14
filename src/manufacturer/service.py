from sqlalchemy.orm import Session

from src.manufacturer.scheme import ManufacturerBase
from src.manufacturer.model import Manufacturer

def create_manufacturer_service(db: Session, 
                                manufacturer: ManufacturerBase):

    manufacturer = Manufacturer(
        name_manufacturer=manufacturer.name_manufacturer
    )

    db.add(manufacturer)
    db.commit()
    db.refresh(manufacturer)
    return manufacturer
    
def get_manufacturer_service(db: Session):
    return db.query(Manufacturer).all()

def delete_manufacturer_service(manufacturer_id: int,
                                db: Session):
    db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).delete()
    db.commit()