from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page
from app.dependencies.roles import get_current_active_user, require_admin
from app.database import get_db
from app.models.user import User
from app.schemas.service import Service, ServiceCreate
from app.crud.service import get_services, create_service, get_service, update_service_by_id, delete_service_by_id

router = APIRouter(tags=["services"])

@router.get("/", response_model=Page[Service])
def read_services(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return get_services(db)

@router.post("/", response_model=Service)
def create_new_service(
    service: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return create_service(db=db, service=service)

@router.get("/{service_id}", response_model=Service)
def read_service(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_service = get_service(db=db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.put("/{service_id}", response_model=Service)
def update_service(
    service_id: int,
    service: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    db_service = update_service_by_id(db=db, service_id=service_id, service_update=service.dict(exclude_unset=True))
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.delete("/{service_id}")
def delete_service(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    db_service = delete_service_by_id(db=db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}