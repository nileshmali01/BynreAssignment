# accounts/views.py

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def account_info(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/account_info.html', context)

@login_required
def track_requests(request):
    user = request.user
    # Assuming you have a related_name in your request model to access requests made by a user
    user_requests = user.user_requests.all()
    context = {
        'user_requests': user_requests,
    }
    return render(request, 'accounts/track_requests.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
