from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .views import (
    RegisterView,
    LoginView,
    AddAppView,
    MyAppsView,
    StartSessionView,
    CheckSessionView,
)


@api_view(['GET'])
def api_root(request):
    return Response({
        "register": request.build_absolute_uri('register/'),
        "login": request.build_absolute_uri('login/'),
        "add_app": request.build_absolute_uri('add-app/'),
        "my_apps": request.build_absolute_uri('my-apps/'),
        "start_session": request.build_absolute_uri('start-session/'),
        "check_session": request.build_absolute_uri('check-session/<session_id>/')
    })


urlpatterns = [
    path('', api_root),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('add-app/', AddAppView.as_view()),
    path('my-apps/', MyAppsView.as_view()),
    path('start-session/', StartSessionView.as_view()),
    path('check-session/<int:session_id>/', CheckSessionView.as_view()),
]