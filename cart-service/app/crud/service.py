from sqlalchemy.orm import Session
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from ..models.service import Service
from ..schemas.service import ServiceCreate

def get_service(db: Session, service_id: int):
    return db.query(Service).filter(Service.id == service_id).first()

def get_services(db: Session, params: Params = Params(page=1, size=10)) -> Page[Service]:
    return paginate(db.query(Service), params)

def get_services_by_type(db: Session, service_type: str, params: Params = Params(page=1, size=10)) -> Page[Service]:
    return paginate(db.query(Service).filter(Service.service_type == service_type), params)

def create_service(db: Session, service: ServiceCreate):
    db_service = Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def update_service_by_id(db: Session, service_id: int, service_update: dict):
    db_service = get_service(db, service_id)
    if not db_service:
        return None
    for key, value in service_update.items():
        setattr(db_service, key, value)
    db.commit()
    db.refresh(db_service)
    return db_service

def delete_service_by_id(db: Session, service_id: int):
    db_service = get_service(db, service_id)
    if not db_service:
        return None
    db.delete(db_service)
    db.commit()
    return db_service