from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.roles import get_current_active_user
from app.database import get_db
from app.models.user import User
from app.schemas.cart import Cart, CartItem, CartItemCreate
from app.crud.cart import get_cart_by_user, add_item_to_cart, remove_item_from_cart, checkout_cart, create_cart
from app.crud.service import get_service

router = APIRouter(tags=["carts"])

@router.get("/", response_model=Cart)
def get_user_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    cart = get_cart_by_user(db, user_id=current_user.id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.post("/items/", response_model=CartItem)
def add_cart_item(
    item: CartItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    service = get_service(db, item.service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    cart = get_cart_by_user(db, user_id=current_user.id)
    if not cart:
        cart = create_cart(db=db, user_id=current_user.id)

    return add_item_to_cart(db, cart_item=item, cart_id=cart.id)

@router.delete("/items/{item_id}")
def remove_cart_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    item = remove_item_from_cart(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item removed successfully"}

@router.post("/checkout/")
def checkout_user_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    cart = get_cart_by_user(db, user_id=current_user.id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return checkout_cart(db, cart_id=cart.id)