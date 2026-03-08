from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta

from .models import MonitoredApp, AppSession
from .serializers import (
    UserSerializer,
    MonitoredAppSerializer,
    AppSessionSerializer,
    LoginSerializer
)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})


class AddAppView(generics.CreateAPIView):
    serializer_class = MonitoredAppSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyAppsView(generics.ListAPIView):
    serializer_class = MonitoredAppSerializer

    def get_queryset(self):
        return MonitoredApp.objects.filter(user=self.request.user)

def check_session_limit(session):
    limit = session.monitored_app.session_limit_minutes
    end_time = session.start_time + timedelta(minutes=limit)

    if timezone.now() >= end_time:
        session.is_active = False
        session.save()

class StartSessionView(generics.CreateAPIView):
    serializer_class = AppSessionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CheckSessionView(APIView):

    def get(self, request, session_id):
        try:
            session = AppSession.objects.get(id=session_id, user=request.user)

            limit = session.monitored_app.session_limit_minutes
            expiry_time = session.start_time + timedelta(minutes=limit)

            if timezone.now() > expiry_time:
                session.is_active = False
                session.save()
                return Response({"status": "expired"})

            return Response({"status": "active"})

        except AppSession.DoesNotExist:
            return Response({"error": "Session not found"}, status=404)


class SessionListView(generics.ListAPIView):
    serializer_class = AppSessionSerializer

    def get_queryset(self):
        sessions = AppSession.objects.filter(user=self.request.user)

        for session in sessions:
            if session.is_active and session.has_expired():
                session.is_active = False
                session.save()

        return sessions