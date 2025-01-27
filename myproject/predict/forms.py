from django import forms
from .models import PredictionData

class PredictionDataForm(forms.ModelForm):
    class Meta:
        model = PredictionData
        fields = ['weather', 'road', 'time', 'package']