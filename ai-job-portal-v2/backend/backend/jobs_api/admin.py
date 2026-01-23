from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'job_type', 'posted_date', 'is_active']
    list_filter = ['job_type', 'location', 'is_active', 'posted_date']
    search_fields = ['title', 'company', 'description']
    list_editable = ['is_active']
    date_hierarchy = 'posted_date'
