from sqlalchemy.orm import Session

from src.product_category.scheme import ProductCategoryBase
from src.product_category.model import ProductCategory

def create_product_category_service(db: Session, 
                                    product_category: ProductCategoryBase):

    product_category = ProductCategory(
        name_category=product_category.name_category
    )

    db.add(product_category)
    db.commit()
    db.refresh(product_category)
    return product_category
    
def get_product_category_service(db: Session):
    return db.query(ProductCategory).all()

def delete_product_category_service(category_id: int,
                                    db: Session):
    db.query(ProductCategory).filter(ProductCategory.id == category_id).delete()
    db.commit()