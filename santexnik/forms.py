from django import forms
from .models import Santexnik

class SantexnikForm(forms.ModelForm):
    class Meta:
        model = Santexnik
        fields = '__all__'
