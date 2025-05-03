from sqlalchemy import Column, Integer, String, Float, Enum
from app.database import Base
from .base import TimestampMixin
from enum import Enum as PyEnum

class ServiceType(str, PyEnum):
    AC_REPAIR = "ac_repair"
    TV_REPAIR = "tv_repair"
    OVEN_REPAIR = "oven_repair"
    IPS_REPAIR = "ips_repair"
    HOME_CLEANING = "home_cleaning"
    REFRIGERATOR_REPAIR = "refrigerator_repair"
    

class Service(Base, TimestampMixin):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))
    base_price = Column(Float)
    service_type = Column(Enum(ServiceType))
    duration_hours = Column(Float)