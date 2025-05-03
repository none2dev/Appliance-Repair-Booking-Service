from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.crud.user import get_user_by_username
from app.database import get_db
from sqlalchemy.orm import Session
from app.enums import UserRole

async def get_current_active_user(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = get_user_by_username(db, username=current_user.username)
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user

async def require_admin(
    current_user: str = Depends(get_current_active_user)
):
    if current_user.role.role_type != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    return current_user

async def require_technician(
    current_user: str = Depends(get_current_active_user)
):
    if current_user.role.role_type not in [UserRole.ADMIN, UserRole.TECHNICIAN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    return current_user