from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import TimestampMixin
from app.database import Base

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    full_name = Column(String(100))
    phone = Column(String(20))
    address = Column(String(255))
    role_id = Column(Integer, ForeignKey("roles.id"))
    is_active = Column(Boolean, default=True)

    role = relationship("Role")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"