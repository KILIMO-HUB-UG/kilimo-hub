from django.db import models

class WeatherCache(models.Model):
    district = models.CharField(max_length=100, unique=True)
    data_json = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
