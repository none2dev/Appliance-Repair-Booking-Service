from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Float
from sqlalchemy.orm import relationship
from app.database import Base
from .base import TimestampMixin
from enum import Enum as PyEnum

class BookingStatus(str, PyEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Booking(Base, TimestampMixin):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    booking_date = Column(DateTime)
    status = Column(String(20), default=BookingStatus.PENDING)
    notes = Column(String(255))
    technician = Column(String(100))
    address = Column(String(255))
    final_price = Column(Float)
    discount_applied = Column(Float, default=0.0)

    user = relationship("User")
    service = relationship("Service")