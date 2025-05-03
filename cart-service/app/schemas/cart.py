from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import List
from .service import Service

class CartStatus(str, Enum):
    active = "active"
    checked_out = "checked_out"
    abandoned = "abandoned"

class CartItemBase(BaseModel):
    service_id: int
    quantity: int = 1

class CartItemCreate(CartItemBase):
    pass

class CartItem(CartItemBase):
    id: int
    service: Service
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CartBase(BaseModel):
    status: CartStatus = CartStatus.active

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    user_id: int
    items: List[CartItem]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True