from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from app.database import Base
from .base import TimestampMixin
from enum import Enum as PyEnum

class DiscountType(str, PyEnum):
    FLAT = "flat"
    PERCENTAGE = "percentage"
    OFF_PEAK = "off_peak"

class Discount(Base, TimestampMixin):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    code = Column(String(50), unique=True)
    discount_type = Column(String(20))
    value = Column(Float)
    valid_from = Column(DateTime)
    valid_to = Column(DateTime)
    is_active = Column(Boolean, default=True)