from fastapi import HTTPException

from sqlalchemy.orm import Session

from src.product.scheme import (ProductBase,
                                DescriptionUpdateBase,
                                PriceUpdateBase,
                                DiscountPriceUpdateBase,
                                QtyUpdateBase,
                                CategoryUpdateBase,
                                ManufacturerUpdate,
                                CharacteristicsUpdate,
                                ListPathImageUpdate,
                                ArticleNumberUpdate,
                                NameProductUpdate)

from src.product.model import Product

def create_product_service(db: Session, 
                            product: ProductBase):

    product = Product(
        name_product=product.name_product,
        description_product=product.description_product,
        list_path_image=product.list_path_image,
        price=product.price,
        discount_price=product.discount_price,
        qty=product.qty,
        category_id=product.category_id,
        article_number=product.article_number,
        manufacturer_id=product.manufacturer_id,
        characteristics=product.characteristics
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    return product
    
def get_product_all_service(db: Session):
    return db.query(Product).all()

def get_product_by_id_service(product_id: int ,db: Session):
    return db.query(Product).filter(Product.id == product_id).first()

def delete_product_service(product_id: int,
                            db: Session):
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()

def update_product_description_service(product_id: int, 
                               new_description: DescriptionUpdateBase, 
                               db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.description_product = new_description.description
    db.commit()
    
    return {"message": "Описание товара успешно обновлено"}

def update_product_price_service(product_id: int,
                                 new_price: PriceUpdateBase,
                                 db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.price = new_price.price
    db.commit()
    
    return {"message": "Цена товара успешно обновлена"}

def update_product_discount_price_service(product_id: int,
                                          new_discount_price: DiscountPriceUpdateBase,
                                          db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.discount_price = new_discount_price.discount_price
    db.commit()
    
    return {"message": "Цена со скидкой успешно обновлена"}

def update_product_qty_service(product_id: int,
                                new_qty: QtyUpdateBase,
                                db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.qty = new_qty.qty
    db.commit()
    
    return {"message": "Количество товара успешно обновлено"}

def update_product_category_service(product_id: int,
                                     new_category_id: CategoryUpdateBase,
                                     db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.category_id = new_category_id.category_id
    db.commit()
    
    return {"message": "Категория товара успешно обновлена"}

def update_product_manufacturer_service(product_id: int,
                                         new_manufacturer_id: ManufacturerUpdate,
                                         db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.manufacturer_id = new_manufacturer_id.manufacturer_id
    db.commit()
    
    return {"message": "Производитель успешно обновлен"}

def update_product_characteristics_service(product_id: int,
                                            new_characteristics: CharacteristicsUpdate,
                                            db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.characteristics = new_characteristics.characteristics
    db.commit()
    
    return {"message": "Характеристики товара успешно обновлены"}
    
def update_product_list_path_image_service(product_id: int,
                                            new_list_path_image: ListPathImageUpdate,
                                            db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.list_path_image = new_list_path_image.list_path_image
    db.commit()
    
    return {"message": "Список изображений успешно обновлен"}

def update_product_article_number_service(product_id: int,
                                           new_article_number: ArticleNumberUpdate,
                                           db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.article_number = new_article_number.article_number
    db.commit()
    
    return {"message": "Артикул успешно обновлен"}

def update_product_list_path_image_service(product_id: int,
                                            new_list_path_image: ListPathImageUpdate,
                                            db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.list_path_image = new_list_path_image.list_path_image
    db.commit()
    
    return {"message": "Список изображений успешно обновлен"}

def update_product_name_service(product_id: int,
                                 new_name: NameProductUpdate,
                                 db: Session):

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    product.name_product = new_name.name_product
    db.commit()
    
    return {"message": "Название товара успешно обновлено"}