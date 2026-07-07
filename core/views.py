from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Alert
from market.models import MarketPrice

@login_required
def dashboard(request):
    alerts = Alert.objects.filter(is_active=True)[:5]
    prices = MarketPrice.objects.order_by('-recorded_at')[:4]
    return render(request, 'core/dashboard.html', {'alerts': alerts, 'prices': prices})

def landing(request):
    return render(request, 'core/landing.html')
