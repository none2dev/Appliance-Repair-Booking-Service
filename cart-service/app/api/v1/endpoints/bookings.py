from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, Params
from app.dependencies.roles import get_current_active_user, require_technician
from app.database import get_db
from app.models.user import User
from app.schemas.booking import Booking, BookingCreate
from app.crud.booking import get_bookings, get_user_bookings, create_booking, update_booking_status_by_technician
from app.crud.discount import get_discount_by_code
from app.crud.service import get_service
from app.enums import DiscountType

router = APIRouter(tags=["bookings"])

@router.get("/", response_model=Page[Booking])
def read_all_bookings(
    params: Params = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_technician)
):
    return get_bookings(db, params=params)

@router.get("/my-bookings", response_model=Page[Booking])
def read_user_bookings(
    params: Params = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return get_user_bookings(db, user_id=current_user.id, params=params)

@router.post("/", response_model=Booking)
def create_new_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    service = get_service(db, booking.service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    discount = get_discount_by_code(db, booking.discount_code)
    if discount and discount.discount_type == DiscountType.PERCENTAGE:
        discount_applied = service.base_price * (discount.value / 100)
    elif discount and discount.discount_type == DiscountType.FLAT:
        discount_applied = discount.value
    else:
        discount_applied = 0.0

    final_price = service.base_price - discount_applied

    return create_booking(db, booking=booking, user_id=current_user.id, final_price=final_price, discount_applied=discount_applied)

@router.put("/{booking_id}/status")
def update_booking_status(
    booking_id: int,
    status: str,
    technician: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_technician)
):
    booking = update_booking_status_by_technician(db, booking_id=booking_id, status=status, technician=technician)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking