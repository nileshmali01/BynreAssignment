from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('account/', views.account_info, name='account_info'),
    path('track/', views.track_requests, name='track_requests'),
    path('login/', LoginView.as_view(), name='login'),
    # Add more URL patterns for login, logout, password reset, etc., as needed
]
