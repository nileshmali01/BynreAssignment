from django import forms
from .models import ServiceRequest
from accounts.forms import CustomerForm  # Import the CustomerForm from the accounts app

class ServiceRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'] = forms.ModelChoiceField(queryset=CustomerForm.Meta.model.objects.all(), required=False)
        self.fields['new_customer_name'] = forms.CharField(max_length=100, required=False)
        self.fields['new_customer_email'] = forms.EmailField(required=False)
    
    class Meta:
        model = ServiceRequest
        fields = ['type_of_request', 'details', 'attached_file', 'customer']  # Adjust fields as needed
