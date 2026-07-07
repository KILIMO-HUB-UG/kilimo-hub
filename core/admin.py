from django.contrib import admin
from .models import FarmerProfile, Alert

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'district', 'phone', 'farm_size_acres']

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['title', 'severity', 'category', 'district', 'created_at', 'is_active']
    list_filter = ['severity', 'category', 'is_active']
