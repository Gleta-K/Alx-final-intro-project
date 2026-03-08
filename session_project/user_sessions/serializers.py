from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MonitoredApp, AppSession


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MonitoredAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoredApp
        fields = '__all__'
        read_only_fields = ['user']


class AppSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSession
        fields = '__all__'
        read_only_fields = ['user', 'start_time']

from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data