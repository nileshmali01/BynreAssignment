from django.urls import path
from accounts.views import track_requests
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', track_requests, name='track_requests'),
    path('request_submitted/', views.request_submitted, name='request_submitted'),
    # Add more URL patterns as needed for other functionalities
]

