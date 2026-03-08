# App Session Tracker API

## Overview
This project is a backend API built with Django REST Framework that allows users to monitor and limit the time spent on specific applications.

Users can:
- Register and log in
- Add apps they want to monitor
- Start app sessions
- Automatically track session limits
- Check if sessions have expired

## Technologies Used
- Python
- Django
- Django REST Framework
- Token Authentication

## API Endpoints

Register
POST /api/register/

Login
POST /api/login/

Add App
POST /api/add-app/

View Apps
GET /api/my-apps/

Start Session
POST /api/start-session/

Check Session
GET /api/check-session/<id>/

View Sessions
GET /api/sessions/

## Setup

Clone repository

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
