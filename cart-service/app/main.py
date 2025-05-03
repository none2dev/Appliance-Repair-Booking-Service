from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import auth, users, services, carts, bookings, discounts, admin
from .models import role, user, service, cart, discount, booking
from app.database import engine, Base
from app.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appliance Repair Booking Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(services.router, prefix="/api/v1/services", tags=["services"])
app.include_router(carts.router, prefix="/api/v1/carts", tags=["carts"])
app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["bookings"])
app.include_router(discounts.router, prefix="/api/v1/discounts", tags=["discounts"])