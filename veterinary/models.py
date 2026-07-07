from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50)
    local_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class VetCondition(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    symptoms = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField(blank=True)
    is_notifiable = models.BooleanField(default=False, help_text="Must be reported to MAAIF")
    severity = models.CharField(max_length=10, choices=[('low','Low'),('medium','Medium'),('high','High')], default='medium')

    def __str__(self):
        return f"{self.name} ({self.animal})"

class VaccineSchedule(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=200)
    disease_prevented = models.CharField(max_length=200)
    first_dose_age = models.CharField(max_length=100)
    booster_interval = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

class VetChatSession(models.Model):
    session_id = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    messages_json = models.TextField(default='[]')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
