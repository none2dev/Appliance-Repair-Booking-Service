from fastapi import APIRouter, Depends, HTTPException, Header, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import AdminCreate, User
from app.crud.user import create_admin_user
from app.config import settings

router = APIRouter(tags=["admin"])

@router.post("/create-admin", response_model=User)
def create_admin(
    admin: AdminCreate,
    request: Request,
    db: Session = Depends(get_db),
    x_admin_secret: str = Header(None)
):
    # Only allow from localhost
    if request.client.host not in ["127.0.0.1", "localhost"]:
        raise HTTPException(
            status_code=403,
            detail="Admin creation only allowed from localhost"
        )
    
    # Verify secret key
    if x_admin_secret != settings.ADMIN_CREATION_SECRET:
        raise HTTPException(
            status_code=403,
            detail="Invalid admin creation secret"
        )

    # Check if feature is enabled
    if not settings.ALLOW_ADMIN_CREATION:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin creation is disabled"
        )
    
    return create_admin_user(db=db, admin=admin)