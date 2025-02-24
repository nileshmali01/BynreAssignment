# accounts/forms.py

from django import forms
from .models import CustomUser

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone_number']  # Adjust fields as needed
