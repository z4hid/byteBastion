# admin.py
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Display these fields in the admin list view
    search_fields = ('name', 'email')  # Enable search by name and email
    list_filter = ('created_at',)  # Add filter options by creation date

admin.site.register(Contact, ContactAdmin)
