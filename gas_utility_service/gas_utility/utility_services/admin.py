from django.contrib import admin

# Register your models here.

from .models import ServiceRequest
admin.site.register(ServiceRequest)
