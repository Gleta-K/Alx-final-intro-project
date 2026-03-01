from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def login_view(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "Use POST to log in",
            "required_fields": ["username", "password"]
        }, status=200)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return JsonResponse(
                    {"error": "Username and password required"},
                    status=400
                )

            # Fake authentication for now
            request.session["username"] = username

            return JsonResponse({
                "message": "Login successful",
                "user": username
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


def protected_view(request):
    username = request.session.get("username")

    if not username:
        return JsonResponse(
            {"error": "Unauthorized. Please log in."},
            status=401
        )

    return JsonResponse({
        "message": "You are authenticated",
        "user": username
    }, status=200)


def logout_view(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Use POST to log out"},
            status=405
        )

    request.session.flush()
    return JsonResponse({"message": "Logged out successfully"}, status=200)