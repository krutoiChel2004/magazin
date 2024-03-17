from sqlalchemy.orm import Session

from src.cart.scheme import ItemCartBase

from src.cart.model import Cart
from src.cart.model import ItemCart

def check_cart_service(db: Session, 
                       user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).first()

def create_cart_service(db: Session, 
                        user_JWT: dict):
    user_id = user_JWT.get("id")
    if check_cart_service(db, user_id):
        return {"message": "Корзина уже существует"}
    db_cart = Cart(user_id=user_id)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return {"message": "Корзина успешно создана",
            "cart": db_cart}

def add_quantity_item_cart_service(item: ItemCart,
                                    db: Session,
                                    qty: int = 1,):
    if item:    
        item.qty += qty
        db.commit()
        db.refresh(item)
        return {"message": "Количество товара в корзине обновлено", "item_cart": item}

def reduce_quantity_item_cart_service(item: ItemCart, 
                                    db: Session,
                                    qty: int = 1,):
    if item:
        item.qty -= qty
        db.commit()
        db.refresh(item)
        return {"message": "Количество товара в корзине обновлено", "item_cart": item}
    
    return {"message": "товара нет в корзине"}

def check_product_in_cart(db: Session, 
                          cart_id: int, 
                          product_id: int):
    item = db.query(ItemCart).filter(ItemCart.cart_id == cart_id, ItemCart.product_id == product_id).first()
    return item

def add_item_cart_service(item_cart: ItemCartBase, 
                          db: Session, 
                          user_JWT: dict):
    user_id = user_JWT.get("id")
    cart_id = check_cart_service(db, user_id).id

    item = check_product_in_cart(db=db, 
                                 cart_id=cart_id, 
                                 product_id=item_cart.product_id)

    if item:
        qty = item_cart.qty
        return add_quantity_item_cart_service(item=item,
                                              qty=qty,
                                              db=db)

    db_item_cart = ItemCart(product_id=item_cart.product_id, 
                            qty=item_cart.qty, 
                            cart_id=cart_id)
    db.add(db_item_cart)
    db.commit()
    db.refresh(db_item_cart)
    return {"message": "Товар добавлен в корзину", "item_cart": db_item_cart}

def get_cart_service(db: Session, 
                     user_JWT: dict):
    user_id = user_JWT.get("id")
    cart_items = db.query(ItemCart).join(Cart).filter(Cart.user_id == user_id).all()
    if not cart_items:
        return {"message": "Корзина не существует"}
    print(cart_items)
    cart_JSON = {"items": [{"id": item.id,
                            "product_id": item.product_id,
                            "qty": item.qty
                            } for item in cart_items]}
    return {"message": "Корзина успешно получена", "cart": cart_JSON}