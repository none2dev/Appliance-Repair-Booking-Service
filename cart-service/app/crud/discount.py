from sqlalchemy.orm import Session
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from datetime import datetime
from ..models.discount import Discount
from ..schemas.discount import DiscountCreate

def get_discount(db: Session, discount_id: int):
    return db.query(Discount).filter(Discount.id == discount_id).first()

def get_discount_by_code(db: Session, code: str):
    return db.query(Discount).filter(Discount.code == code).first()

def get_active_discounts(db: Session, params: Params = Params(page=1, size=10)) -> Page[Discount]:
    now = datetime.now()
    return paginate(
        db.query(Discount).filter(
            Discount.is_active == True,
            Discount.valid_from <= now,
            Discount.valid_to >= now
        ),
        params
    )

def create_discount(db: Session, discount: DiscountCreate):
    db_discount = Discount(**discount.dict())
    db.add(db_discount)
    db.commit()
    db.refresh(db_discount)
    return db_discount

def update_discount(db: Session, discount_id: int, discount_update: dict):
    db_discount = get_discount(db, discount_id)
    if not db_discount:
        return None
    for key, value in discount_update.items():
        setattr(db_discount, key, value)
    db.commit()
    db.refresh(db_discount)
    return db_discount

def deactivate_discount(db: Session, discount_id: int):
    db_discount = get_discount(db, discount_id)
    if not db_discount:
        return None
    db_discount.is_active = False
    db.commit()
    db.refresh(db_discount)
    return db_discount