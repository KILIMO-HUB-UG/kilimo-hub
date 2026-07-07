from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Disease, DiseaseReport
from .forms import DiseaseReportForm

@login_required
def disease_list(request):
    diseases = Disease.objects.all()
    crop_filter = request.GET.get('crop')
    if crop_filter:
        diseases = diseases.filter(crop_affected__icontains=crop_filter)
    return render(request, 'disease/list.html', {'diseases': diseases})

def report_disease(request):
    if request.method == 'POST':
        form = DiseaseReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()
            # In production: call AI vision API here for diagnosis
            report.ai_diagnosis = "Fall Armyworm (Spodoptera frugiperda) detected with high probability. Ragged leaf margins and frass visible in whorl."
            report.ai_confidence = 0.87
            report.status = 'identified'
            report.save()
            messages.success(request, 'Your report has been submitted. AI diagnosis below.')
            return redirect('disease:report_result', pk=report.pk)
    else:
        form = DiseaseReportForm()
    return render(request, 'disease/report.html', {'form': form})

def report_result(request, pk):
    from django.shortcuts import get_object_or_404
    report = get_object_or_404(DiseaseReport, pk=pk)
    return render(request, 'disease/result.html', {'report': report})
