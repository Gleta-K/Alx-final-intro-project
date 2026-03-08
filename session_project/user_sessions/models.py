from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MonitoredApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=100)
    session_limit_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.app_name}"


class AppSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monitored_app = models.ForeignKey(MonitoredApp, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monitored_app = models.ForeignKey(MonitoredApp, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def has_expired(self):
        limit = self.monitored_app.session_limit_minutes
        end_time = self.start_time + timedelta(minutes=limit)
        return timezone.now() >= end_time
    
    def __str__(self):
        return f"{self.user.username} - {self.monitored_app.app_name}"