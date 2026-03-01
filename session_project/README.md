# Session Authentication API (Django)

## Project Description
This project demonstrates session-based authentication using Django. 
Users can log in, access protected routes, and log out using Django sessions.

## Features
- Session-based authentication
- Login endpoint
- Protected endpoint
- Logout endpoint
- Admin panel access

## API Endpoints

### API Root
GET /api/

Returns available endpoints.

### Login
POST /api/login/

Body:
{
  "username": "your_username",
  "password": "your_password"
}

### Protected Route
GET /api/protected/

Requires active session.

### Logout
POST /api/logout/

Destroys active session.

## Installation

1. Clone repository
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Run migrations:

python manage.py migrate

5. Create superuser:

python manage.py createsuperuser

6. Run server:

python manage.py runserver

## Admin Panel
http://127.0.0.1:8000/admin/
