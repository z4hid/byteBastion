from django.contrib import admin

# Register your models here.
# leak/admin.py
from django.contrib import admin
from .models import LeakResult
from .models import LeakResult

@admin.register(LeakResult)
class LeakCheckResultAdmin(admin.ModelAdmin):
    list_display = ('username_or_email', 'found_count', 'created_at')
    search_fields = ('username_or_email',)
    readonly_fields = ('created_at',)
