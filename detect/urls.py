# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('detect/', views.upload_page, name='upload_page'),
]