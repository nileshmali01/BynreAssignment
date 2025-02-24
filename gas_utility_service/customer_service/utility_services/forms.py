# utility_services/forms.py

from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['type_of_request', 'details', 'attached_file']  # Add other fields as needed
