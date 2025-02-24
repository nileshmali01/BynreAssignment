from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='submit/')),  # Redirect root URL to submit/ endpoint
    path('', include('utility_services.urls')),  # Include app's URLs here
]
