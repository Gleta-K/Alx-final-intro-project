from django.contrib import admin
from .models import MonitoredApp, AppSession

# Register your models here.
admin.site.register(MonitoredApp)
admin.site.register(AppSession)