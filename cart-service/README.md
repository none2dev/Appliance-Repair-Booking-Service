# Appliance-Repair-Booking-Service -- Cart Service
Python: 3.12.9

ERD (Entity Relationship Diagram)
+----------------+       +----------------+       +-------------------+
|     Users      |       |     Roles      |       |    Services       |
+----------------+       +----------------+       +-------------------+
| PK: id         |<----->| PK: id         |       | PK: id            |
|    username    |       |    name        |       |    name           |
|    email       |       |    description |       |    description    |
|    password    |       +----------------+       |    base_price     |
|    full_name   |                               |    service_type   |
|    phone       |                               |    duration_hours |
|    address     |                               +-------------------+
| FK: role_id    |                                       ^
|    is_active   |                                       |
|    created_at  |                                       |
|    updated_at  |                               +-------------------+
+----------------+                               |    CartItems      |
        ^                                        +-------------------+
        |                                        | PK: id            |
+----------------+       +----------------+      | FK: user_id       |
|    Bookings    |       |     Carts      |      | FK: service_id    |
+----------------+       +----------------+      |    quantity       |
| PK: id         |       | PK: id         |      |    added_at       |
| FK: user_id    |       | FK: user_id    |      +-------------------+
| FK: service_id |       |    status      |              ^
|    booking_date|       |    created_at  |              |
|    status      |       |    updated_at  |      +-------------------+
|    notes       |       +----------------+      |    Discounts      |
|    technician  |               ^               +-------------------+
|    address     |               |               | PK: id            |
|    created_at  |       +----------------+      |    name           |
|    updated_at  |       |  BookingItems  |      |    code           |
+----------------+       +----------------+      |    discount_type  |
                        | PK: id         |      |    value          |
                        | FK: booking_id |      |    valid_from     |
                        | FK: service_id  |      |    valid_to       |
                        |    quantity     |      |    is_active      |
                        |    price        |      +-------------------+
                        +----------------+
						

Project Structure
appliance-repair-booking-cart-service/
├── .env
├── alembic/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── service.py
│   │   ├── cart.py
│   │   ├── booking.py
│   │   └── discount.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── service.py
│   │   ├── cart.py
│   │   ├── booking.py
│   │   └── discount.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── service.py
│   │   ├── cart.py
│   │   ├── booking.py
│   │   └── discount.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       ├── auth.py
│   │   │       ├── users.py
│   │   │       ├── services.py
│   │   │       ├── admin.py
│   │   │       ├── carts.py
│   │   │       ├── bookings.py
│   │   │       └── discounts.py
│   │   │   
│   ├── core/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── security.py
│   ├── dependencies/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── roles.py
│   └── utils/
│       ├── __init__.py
│       ├── discount.py
│       └── pricing.py
├── tests/
├── requirements.txt
├── alembic.ini
└── README.md


Database Migrations:
alembic upgrade head


Run the Application
uvicorn app.main:app --reload