from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    AddAppView,
    MyAppsView,
    StartSessionView,
    CheckSessionView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('add-app/', AddAppView.as_view()),
    path('my-apps/', MyAppsView.as_view()),
    path('start-session/', StartSessionView.as_view()),
    path('check-session/<int:session_id>/', CheckSessionView.as_view()),
]