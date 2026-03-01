from django.urls import path
from .views import login_view, protected_view, logout_view
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "available_endpoints": [
            "/api/login/",
            "/api/protected/",
            "/api/logout/"
        ]
    })
urlpatterns = [
    path('', api_root),
    path("login/", login_view),
    path("protected/", protected_view),
    path("logout/", logout_view),
]