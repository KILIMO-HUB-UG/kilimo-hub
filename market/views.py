from django.shortcuts import render
from .models import Market, Commodity, MarketPrice


def price_list(request):
    commodity_name = request.GET.get('commodity', 'Maize')
    commodities = Commodity.objects.all()
    try:
        commodity = Commodity.objects.get(name__iexact=commodity_name)
        prices = MarketPrice.objects.filter(commodity=commodity).select_related('market').order_by('-recorded_at')[:20]
    except Commodity.DoesNotExist:
        commodity = None
        prices = MarketPrice.objects.select_related('market', 'commodity').order_by('-recorded_at')[:20]
    return render(request, 'market/prices.html', {
        'prices': prices, 'commodities': commodities, 'selected_commodity': commodity
    })


def market_list(request):
    markets = Market.objects.all()
    return render(request, 'market/markets.html', {'markets': markets})
