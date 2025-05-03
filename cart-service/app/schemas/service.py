from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from app.enums import ServiceType


class ServiceBase(BaseModel):
    name: str
    description: str
    base_price: float
    service_type: ServiceType
    duration_hours: float

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True