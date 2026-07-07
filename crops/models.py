from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    name = models.CharField(max_length=100)
    local_name = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='crops/', blank=True)
    days_to_maturity_min = models.IntegerField()
    days_to_maturity_max = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CropCalendar(models.Model):
    MONTH_CHOICES = [(i, m) for i, m in enumerate(
        ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], 1)]
    ACTIVITY_CHOICES = [
        ('land_prep', 'Land Preparation'), ('planting', 'Planting'),
        ('weeding', 'Weeding'), ('fertilizing', 'Fertilizing'),
        ('pest_control', 'Pest Control'), ('harvest', 'Harvest'),
    ]
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='calendar_entries')
    district = models.CharField(max_length=50, blank=True)
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    month = models.IntegerField(choices=MONTH_CHOICES)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['month']

class FarmerCrop(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farm_crops')
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety = models.CharField(max_length=100, blank=True)
    planted_date = models.DateField()
    area_acres = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-planted_date']

    def __str__(self):
        return f"{self.farmer.username} — {self.crop.name} ({self.planted_date})"

class CropAdvisoryChat(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField()
    answer = models.TextField()
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
