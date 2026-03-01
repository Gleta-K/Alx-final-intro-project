from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "application": "SessionGuard API",
        "status": "running",
        "available_endpoints": {
            "register": "/api/register/",
            "login": "/api/login/",
            "logout": "/api/logout/",
            "add_app": "/api/add-app/",
            "my_apps": "/api/my-apps/",
            "start_session": "/api/start-session/",
            "check_session": "/api/check-session/"
        }
    })


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('user_sessions.urls')),
]