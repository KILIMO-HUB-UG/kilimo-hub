from django.contrib import admin
from .models import Animal, VetCondition, VaccineSchedule
admin.site.register(Animal)
admin.site.register(VetCondition)
admin.site.register(VaccineSchedule)
