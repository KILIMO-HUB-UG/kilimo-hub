from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Animal, VetCondition, VaccineSchedule

@login_required
def vet_home(request):
    animals = Animal.objects.all()
    vaccines = VaccineSchedule.objects.select_related('animal').all()
    return render(request, 'veterinary/home.html', {'animals': animals, 'vaccines': vaccines})

@require_POST
def vet_chat(request):
    data = json.loads(request.body)
    question = data.get('question', '').lower()
    answers = {
        'fever': "Fever in cattle may indicate East Coast Fever (ECF), Foot & Mouth Disease, or Trypanosomiasis. Check body temperature (normal: 38–39.5°C). Isolate the animal and contact Dr. Agaba or the nearest MAAIF vet immediately.",
        'newcastle': "Newcastle disease in poultry: vaccinate with Lasota every 3 months. Infected birds show nervous signs, green diarrhoea, and respiratory distress. Isolate and notify your district vet.",
        'fmd': "Foot & Mouth Disease: blisters on feet, mouth, and teats. Highly contagious — isolate immediately. Report to MAAIF. This is a notifiable disease in Uganda.",
        'lsd': "Lumpy Skin Disease (LSD): firm nodules on skin. Vaccinate healthy herd immediately. No cure — supportive care only. Notify MAAIF.",
        'default': "Please describe your animal's symptoms in detail (species, age, symptoms, duration). I'll give you advice and recommend whether to contact a vet immediately.",
    }
    if any(w in question for w in ['fever', 'temperature', 'hot']):
        answer = answers['fever']
    elif 'newcastle' in question or 'poultry' in question or 'chicken' in question:
        answer = answers['newcastle']
    elif 'fmd' in question or 'foot' in question or 'mouth' in question:
        answer = answers['fmd']
    elif 'lumpy' in question or 'lsd' in question or 'nodule' in question:
        answer = answers['lsd']
    else:
        answer = answers['default']
    return JsonResponse({'answer': answer})
