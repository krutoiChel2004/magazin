from sqlalchemy.orm import Session

from src.product.scheme import ProductBase
from src.product.model import Product

def create_product_service(db: Session, 
                            product: ProductBase):

    product = Product(
        name_product=product.name_product,
        description_product=product.description_product,
        price=product.price,
        discount_price=product.discount_price,
        qty=product.qty,
        category_id=product.category_id,
        article_number=product.article_number,
        manufacturer_id=product.manufacturer_id,
        characteristic=product.characteristics
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    return product
    
def get_product_service(db: Session):
    return db.query(Product).all()

def delete_product_service(product_id: int,
                                db: Session):
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()