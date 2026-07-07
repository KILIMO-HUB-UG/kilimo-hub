from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Crop, CropCalendar, FarmerCrop

@login_required
def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'crops/list.html', {'crops': crops})

def crop_detail(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    calendar = CropCalendar.objects.filter(crop=crop)
    return render(request, 'crops/detail.html', {'crop': crop, 'calendar': calendar})

def my_crops(request):
    farm_crops = FarmerCrop.objects.filter(farmer=request.user) if request.user.is_authenticated else []
    return render(request, 'crops/my_crops.html', {'farm_crops': farm_crops})

@require_POST
def crop_chat(request):
    """Simple AI crop advisory endpoint — returns mock advice for demo."""
    data = json.loads(request.body)
    question = data.get('question', '')
    responses = {
        'harvest': 'Based on typical growth cycles, check for husk drying and brown silks as harvest indicators.',
        'fertilizer': 'Apply CAN (Calcium Ammonium Nitrate) at 50kg/acre for top-dressing maize at tasseling stage.',
        'pest': 'Scout for Fall Armyworm in maize whorls. Apply Emamectin benzoate if >2 larvae per plant.',
        'default': 'For personalized advice, describe your crop, growth stage, and the specific challenge you are facing.',
    }
    q = question.lower()
    if any(w in q for w in ['harvest', 'ready', 'maturity']):
        answer = responses['harvest']
    elif any(w in q for w in ['fertiliz', 'npk', 'urea', 'can']):
        answer = responses['fertilizer']
    elif any(w in q for w in ['pest', 'worm', 'insect', 'disease']):
        answer = responses['pest']
    else:
        answer = responses['default']
    return JsonResponse({'answer': answer})
