from sqlalchemy import Column, Integer, String, Enum
from .base import TimestampMixin
from app.database import Base
from app.enums import UserRole

class Role(Base, TimestampMixin):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(255), nullable=True)
    role_type = Column(Enum(UserRole))

    def __repr__(self):
        return f"<Role(name='{self.name}')>"