from django.contrib import admin
from .models import Crop, CropCalendar, FarmerCrop
admin.site.register(Crop)
admin.site.register(CropCalendar)
admin.site.register(FarmerCrop)
