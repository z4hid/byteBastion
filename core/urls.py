# urls.py
from django.urls import path
from . views import HomeView, SolutionsView, contact_view, success_view
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('solutions/', SolutionsView.as_view(), name='solutions'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    # path('passwords/', views.password_list, name='password_list'),
    # path('add_passowrd/', views.add_password, name='add_password'),
]
