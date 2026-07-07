from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, blank=True)
    crop_affected = models.CharField(max_length=100)
    symptoms = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField(blank=True)
    severity = models.CharField(max_length=10, choices=[('low','Low'),('medium','Medium'),('high','High')], default='medium')
    image = models.ImageField(upload_to='diseases/', blank=True)

    def __str__(self):
        return f"{self.name} ({self.crop_affected})"

class DiseaseReport(models.Model):
    STATUS_CHOICES = [('pending','Pending'),('identified','Identified'),('confirmed','Confirmed')]
    photo = models.ImageField(upload_to='disease_reports/')
    description = models.TextField(blank=True)
    district = models.CharField(max_length=100, blank=True)
    crop_name = models.CharField(max_length=100, blank=True)
    ai_diagnosis = models.TextField(blank=True)
    ai_confidence = models.FloatField(null=True, blank=True)
    identified_disease = models.ForeignKey(Disease, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    reporter_phone = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ['-submitted_at']
