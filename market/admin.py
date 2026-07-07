from django.contrib import admin
from .models import Market, Commodity, MarketPrice, PriceAlert
admin.site.register(Market)
admin.site.register(Commodity)
admin.site.register(MarketPrice)
admin.site.register(PriceAlert)
