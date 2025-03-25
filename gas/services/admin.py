from django.contrib import admin
from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "request_type",
        "status",
        "priority",
        "submitted_date",
        "resolved_date",
    )
    list_filter = ("status", "priority", "submitted_date")
    search_fields = ("customer__username", "details")
