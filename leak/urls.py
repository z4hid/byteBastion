from django.urls import path
from . import views

urlpatterns = [
    path('breach/', views.check_leak, name='check_leak'),
]