# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        # Handles root URL
    path('about/', views.about, name='about') # Handles /about/
]
