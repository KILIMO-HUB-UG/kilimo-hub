from django import forms
from .models import DiseaseReport

class DiseaseReportForm(forms.ModelForm):
    class Meta:
        model = DiseaseReport
        fields = ['photo', 'crop_name', 'description', 'district', 'reporter_phone']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe what you see...'}),
        }
