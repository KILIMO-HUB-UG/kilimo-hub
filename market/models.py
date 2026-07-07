from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.name} — {self.district}"

class Commodity(models.Model):
    UNIT_CHOICES = [('kg', 'per kg'), ('bag', 'per bag (100kg)'), ('bunch', 'per bunch'), ('head', 'per head')]
    name = models.CharField(max_length=100)
    local_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, default='crop')
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='kg')

    def __str__(self):
        return self.name

class MarketPrice(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='prices')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='prices')
    price_ugx = models.DecimalField(max_digits=10, decimal_places=2)
    price_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    recorded_by = models.CharField(max_length=100, default='Kilimo Hub Agent')

    class Meta:
        ordering = ['-recorded_at']
        get_latest_by = 'recorded_at'

    def __str__(self):
        return f"{self.commodity.name} @ {self.market.name}: UGX {self.price_ugx}"

class PriceAlert(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    alert_above = models.BooleanField(default=True, help_text="Alert when price goes above target")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
