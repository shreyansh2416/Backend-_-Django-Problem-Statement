"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from services import views

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),

    # Service request URLs
    path('create/', views.create_request, name='create-request'),
    path('my-requests/', views.my_requests, name='my-requests'),

    # Redirect root URL (fixed closing quote)
    path('', RedirectView.as_view(url='/my-requests/')),
]