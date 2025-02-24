from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_submitted')  # Redirect to 'request_submitted' URL upon successful submission
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def track_request(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'track_request.html', {'requests': requests})

def request_submitted(request):
    return render(request, 'request_submitted.html')  # Assuming you have a template named 'request_submitted.html'
