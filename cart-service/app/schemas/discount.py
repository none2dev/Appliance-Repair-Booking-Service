from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class DiscountType(str, Enum):
    flat = "flat"
    percentage = "percentage"
    off_peak = "off_peak"

class DiscountBase(BaseModel):
    name: str
    code: str
    discount_type: DiscountType
    value: float
    valid_from: datetime
    valid_to: datetime
    is_active: bool = True

class DiscountCreate(DiscountBase):
    pass

class Discount(DiscountBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True