SessionGuard API

SessionGuard API is a backend web application developed using Django and Django REST Framework. The system allows users to register, authenticate, and manage monitored applications by setting time-based session limits. When a session exceeds the configured time limit, the system marks it as expired and enforces logout logic within the application.

This project demonstrates backend web development concepts including RESTful API design, authentication, database modeling, session management, and business logic implementation.

Technology Stack

The application is built using Python 3, Django, Django REST Framework, and SQLite as the default database. Token-based authentication is used to secure API endpoints.

System Overview

The system allows users to create accounts and log in using token authentication. After authentication, users can register applications they wish to monitor, specify a time limit in minutes, and start usage sessions. The backend tracks the session start time and compares it with the configured time limit. If the session duration exceeds the limit, the session is marked as expired.

This structure demonstrates relational database modeling through the use of foreign key relationships between users, monitored applications, and sessions.

Project Structure

The project contains a Django project directory named session_project and an application directory named user_sessions. The user_sessions application contains the models, serializers, views, and URL configurations responsible for handling API requests. The root project directory contains global settings, main URL configuration, and the manage.py file used for running the application.

API Endpoints

The system provides endpoints for user registration, login, logout, application registration, session creation, and session validation. All protected endpoints require token authentication.

POST /api/register/ allows a new user to create an account.
POST /api/login/ authenticates a user and returns an authentication token.
POST /api/logout/ invalidates the user session.
POST /api/add-app/ allows an authenticated user to register a monitored application.
GET /api/my-apps/ retrieves the list of applications registered by the user.
POST /api/start-session/ starts a new session for a monitored application.
GET /api/check-session/ checks whether a session has exceeded its configured time limit.

Authentication

The API uses token-based authentication. After logging in, the user receives a token which must be included in the Authorization header of subsequent requests using the following format:

Authorization: Token your_token_here

Requests made without a valid token will be denied access to protected endpoints.