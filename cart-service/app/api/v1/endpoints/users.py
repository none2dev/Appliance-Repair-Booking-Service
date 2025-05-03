from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page
from app.dependencies.roles import get_current_active_user, require_admin
from app.database import get_db
from app.schemas.user import User, UserCreate, UserUpdate
from app.crud.user import get_users, create_user, get_user, update_user, delete_user

router = APIRouter(tags=["users"])

@router.get("/", response_model=Page[User])
def read_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return get_users(db)

@router.post("/", response_model=User)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return create_user(db=db, user=user)

@router.get("/{user_id}", response_model=User)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User)
def update_existing_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_user = update_user(db, user_id=user_id, user_update=user.dict(exclude_unset=True))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}")
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}