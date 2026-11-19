# FoodFlow – Food Ordering & Restaurant Management API

A backend application built with **FastAPI and MySQL** that provides REST APIs for food ordering, restaurant management, menu management and order tracking.

## Project Overview

FoodFlow is a food ordering backend designed to connect customers with restaurants. It provides APIs for user authentication, restaurant discovery, menu management and order processing.

The project follows a modular backend architecture to separate API routes, business logic, database operations and data validation.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Database Driver:** PyMySQL
- **Data Validation:** Pydantic
- **Authentication:** JWT (JSON Web Tokens)
- **Password Security:** Password Hashing with pwdlib
- **Database Migrations:** Alembic
- **API Testing:** Swagger UI, Postman
- **Version Control:** Git, GitHub

## Features

### 1. Authentication
- User registration and login.
- Password hashing for secure password storage.
- JWT-based authentication.
- Customer and restaurant role assignment during registration.

### 2. Restaurant Management
- Create restaurant profiles.
- Retrieve restaurant information.
- Update restaurant details.
- Delete restaurant records.

### 3. Menu Management
- Create menu items.
- Retrieve menu items by restaurant.
- Retrieve individual menu items.
- Update menu details.

### 4. Order Management
- Place food orders.
- Calculate order totals based on menu item prices and quantities.
- Validate menu item availability.
- Verify that menu items belong to the selected restaurant.
- Retrieve individual order details.
- View customer order history.
- Cancel pending orders.

### 5. Authorization
- JWT-based user identification.
- Customer ownership verification when accessing and cancelling orders.
- Role assignment stored in the database.

## Project Architecture

The project follows a layered architecture:

```text
Client Request
      |
      v
    Router
      |
      v
    Schema
      |
      v
    Service Layer
      |
      v
  Repository Layer
      |
      v
  SQLAlchemy ORM
      |
      v
    MySQL
```

**Layer responsibilities:**

- **Router:** Handles HTTP requests and responses.
- **Schema:** Validates incoming data and structures API responses.
- **Service:** Implements business logic and validation.
- **Repository:** Handles database queries and operations.
- **Model:** Defines database tables and relationships.
- **Database:** Stores application data in MySQL.

## API Endpoints

Base URL: `http://127.0.0.1:8000`

| Module | Method | Endpoint | Description |
|---|---|---|---|
| Authentication | POST | `/auth/register` | Register a user |
| Authentication | POST | `/auth/login` | User login |
| Restaurants | POST | `/restaurants/` | Create restaurant |
| Restaurants | GET | `/restaurants/` | Get restaurants |
| Restaurants | GET | `/restaurants/{id}` | Get restaurant details |
| Restaurants | PUT | `/restaurants/{id}` | Update restaurant |
| Restaurants | DELETE | `/restaurants/{id}` | Delete restaurant |
| Menu | POST | `/menu/` | Create menu item |
| Menu | GET | `/menu/restaurant/{restaurant_id}` | Get restaurant menu |
| Menu | GET | `/menu/{menu_id}` | Get menu item |
| Menu | PUT | `/menu/{menu_id}` | Update menu item |
| Orders | POST | `/orders/` | Place an order |
| Orders | GET | `/orders/` | Get customer order history |
| Orders | GET | `/orders/{order_id}` | Get order details |
| Orders | PATCH | `/orders/{order_id}/cancel` | Cancel pending order |

## Database Design

The application uses MySQL with SQLAlchemy ORM.

Main entities include:

- Users
- Restaurants
- Menu Items
- Orders
- Order Items

Relationships and foreign keys maintain data consistency between related records.

Alembic is used to manage database schema migrations.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/parulAIML022/Foodflow.git
cd Foodflow
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and configure the MySQL connection and application secrets according to `app/core/config.py`.

Do not commit your `.env` file or expose database credentials and JWT secrets.

### 6. Run database migrations

```bash
alembic upgrade head
```

### 7. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

### 8. Explore API documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive API documentation and allows you to test the endpoints.

## Learning Outcomes

Through this project, I gained practical experience in:

- Building RESTful APIs using FastAPI.
- Implementing JWT authentication.
- Understanding authentication and authorization.
- Designing relational databases using MySQL.
- Working with SQLAlchemy ORM and Alembic migrations.
- Implementing layered backend architecture.
- Writing business logic and handling API exceptions.
- Testing APIs using Swagger UI.

## Author

**Parul Chilongia**

GitHub: https://github.com/parulAIML022

---

*FoodFlow – A practical backend development project built using Python and FastAPI.*
