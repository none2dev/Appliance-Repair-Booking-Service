from sqlalchemy.orm import Session
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from ..models.cart import Cart, CartItem
from ..schemas.cart import CartCreate, CartItemCreate

def get_cart(db: Session, cart_id: int):
    return db.query(Cart).filter(Cart.id == cart_id).first()

def get_cart_by_user(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id, Cart.status == "active").first()

def get_carts(db: Session, params: Params = Params(page=1, size=10)) -> Page[Cart]:
    return paginate(db.query(Cart), params)

def create_cart(db: Session, user_id: int):
    cart = CartCreate()
    db_cart = Cart(**cart.model_dump(), user_id=user_id)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def add_item_to_cart(db: Session, cart_item: CartItemCreate, cart_id: int):
    db_item = CartItem(**cart_item.model_dump(), cart_id=cart_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def remove_item_from_cart(db: Session, item_id: int):
    db_item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item

def checkout_cart(db: Session, cart_id: int):
    db_cart = get_cart(db, cart_id)
    if not db_cart:
        return None
    db_cart.status = "checked_out"
    db.commit()
    db.refresh(db_cart)
    return db_cart