from django.db import models
from django.contrib.auth.models import User


class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ("REP", "Repair"),
        ("INST", "Installation"),
        ("BILL", "Billing"),
        ("SAFE", "Safety Inspection"),
    ]
    STATUS_CHOICES = [
        ("PEN", "Pending"),
        ("PRO", "In Progress"),
        ("RES", "Resolved"),
    ]
    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MED", "Medium"),
        ("HIGH", "High"),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=4, choices=REQUEST_TYPES)
    details = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="PEN")
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default="MED")
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    attached_file = models.FileField(
        upload_to="request_attachments/", null=True, blank=True
    )
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.status}"
