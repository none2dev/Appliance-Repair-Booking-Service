from sqlalchemy.orm import Session
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from ..models.booking import Booking
from ..schemas.booking import BookingCreate


def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

def get_bookings(db: Session, params: Params = Params(page=1, size=10)) -> Page[Booking]:
    return paginate(db.query(Booking), params)

def get_user_bookings(db: Session, user_id: int, params: Params = Params(page=1, size=10)) -> Page[Booking]:
    return paginate(db.query(Booking).filter(Booking.user_id == user_id), params)

def create_booking(db: Session, booking: BookingCreate, user_id: int, final_price: float, discount_applied: float = 0.0):
    db_booking = Booking(
        **booking.model_dump(exclude={"discount_code"}),
        user_id=user_id,
        final_price=final_price,
        discount_applied=discount_applied
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def update_booking_status_by_technician(db: Session, booking_id: int, status: str, technician: str = None):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        return None
    db_booking.status = status
    if technician:
        db_booking.technician = technician
    db.commit()
    db.refresh(db_booking)
    return db_booking