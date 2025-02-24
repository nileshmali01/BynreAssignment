from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from accounts.models import CustomUser

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if an existing customer is selected
            customer_id = form.cleaned_data.get('customer')
            if customer_id:
                customer = CustomUser.objects.get(id=customer_id)
            else:
                # Create a new customer if not selected
                new_customer_name = form.cleaned_data.get('new_customer_name')
                new_customer_email = form.cleaned_data.get('new_customer_email')
                # Create a new user with the provided name and email
                customer = CustomUser.objects.create_user(email=new_customer_email, name=new_customer_name)
            
            # Save the service request with the selected or new customer
            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            
            return redirect('request_submitted')  # Redirect to 'request_submitted' URL upon successful submission
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def request_submitted(request):
    return render(request, 'utility_services/request_submitted.html')
