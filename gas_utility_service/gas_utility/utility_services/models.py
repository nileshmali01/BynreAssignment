# utility_services/models.py

from django.db import models
from django.conf import settings  # Import the settings module

from accounts.models import CustomUser  # Import the Customer model from the accounts app

class ServiceRequest(models.Model):
    class Meta:
        app_label = 'utility_services'  # Add this line

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_of_request = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)
    attached_file = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f"Request {self.id} - {self.type_of_request} ({self.status})"
