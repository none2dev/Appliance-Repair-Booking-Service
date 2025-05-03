from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, Params
from app.dependencies.roles import require_admin, get_current_active_user
from app.database import get_db
from app.schemas.discount import Discount, DiscountCreate
from app.crud.discount import get_active_discounts, create_discount, update_discount, deactivate_discount
from app.models.user import User

router = APIRouter(tags=["discounts"])

@router.get("/", response_model=Page[Discount])
def read_active_discounts(
    params: Params = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return get_active_discounts(db, params=params)

@router.post("/", response_model=Discount)
def create_new_discount(
    discount: DiscountCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return create_discount(db, discount=discount)

@router.put("/{discount_id}", response_model=Discount)
def update_existing_discount(
    discount_id: int,
    discount: DiscountCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    db_discount = update_discount(db, discount_id=discount_id, discount_update=discount.dict(exclude_unset=True))
    if not db_discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return db_discount

@router.delete("/{discount_id}")
def deactivate_existing_discount(
    discount_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    discount = deactivate_discount(db, discount_id=discount_id)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return {"message": "Discount deactivated successfully"}