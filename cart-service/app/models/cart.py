from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.database import Base
from .base import TimestampMixin
from enum import Enum as PyEnum
from .user import User

class CartStatus(str, PyEnum):
    ACTIVE = "active"
    CHECKED_OUT = "checked_out"
    ABANDONED = "abandoned"

class Cart(Base, TimestampMixin):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String(20), default=CartStatus.ACTIVE)

    user = relationship("User")
    items = relationship("CartItem", back_populates="cart")

class CartItem(Base, TimestampMixin):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    quantity = Column(Integer, default=1)

    cart = relationship("Cart", back_populates="items")
    service = relationship("Service")