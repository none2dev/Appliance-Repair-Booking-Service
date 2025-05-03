from pydantic import BaseModel
from enum import Enum as PyEnum
from datetime import datetime
from typing import Optional
from .service import Service

class BookingStatus(str, PyEnum):
    pending = "pending"
    confirmed = "confirmed"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class BookingBase(BaseModel):
    service_id: int
    booking_date: datetime
    address: str
    notes: Optional[str] = None
    discount_code: Optional[str] = None

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    user_id: int
    status: BookingStatus
    technician: Optional[str] = None
    final_price: float
    discount_applied: float
    service: Service
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True