# Appliance-Repair-Booking-Service
# Cart Service

A microservice for managing shopping carts in the Appliance Repair Booking System. This service handles cart operations including adding/removing services, managing quantities, and checkout functionality.

## Features

- **Cart Management**:
  - Create and manage user carts
  - Add/remove repair services (AC, TV, Oven)
  - Update service quantities
  - Cart status tracking (active, checked out, abandoned)

- **Integration**:
  - Service catalog integration
  - User authentication
  - Booking system synchronization

- **Pagination & Filtering**:
  - Paginated cart listings
  - Filter by cart status

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Authentication**: JWT
- **Pagination**: fastapi-pagination
- **Containerization**: Docker
- **Testing**: Pytest
- **API Documentation**: Swagger UI & ReDoc

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL 13+
- Docker (optional)
- Python Version Tested: 3.12.9

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/none2dev/Appliance-Repair-Booking-Service.git
   cd cart-service
   
2. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

3. Install dependencies:
    ```bash
   pip install -r requirements.txt

4. Set up environment variables:
    ```bash
   cp .env.example .env

    Edit .env with your configuration.

5. Create PostgreSQL database:
    ```bash
   CREATE DATABASE cart_service;

6. Run migrations:
    ```bash
   alembic upgrade head

7. Running the Service:
    ```bash
   uvicorn app.main:app --reload
