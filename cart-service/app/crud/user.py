from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..models.user import User
from ..schemas.user import UserCreate, AdminCreate
from ..core.auth import get_password_hash
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, params: Params = Params(page=1, size=10)) -> Page:
    return paginate(db.query(User), params)

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        full_name=user.full_name,
        phone=user.phone,
        address=user.address,
        role_id=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_admin_user(db: Session, admin: AdminCreate):
    hashed_password = get_password_hash(admin.password)
    db_user = User(
        username=admin.username,
        email=admin.email,
        password=hashed_password,
        full_name=admin.full_name,
        role_id=1
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: dict):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user_update.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user