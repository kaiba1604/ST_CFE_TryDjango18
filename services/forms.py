from .models import ServiceRequest
from django import forms

class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        exclude =['requested','manager','staff']