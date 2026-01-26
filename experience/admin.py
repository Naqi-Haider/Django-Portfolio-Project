from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'experience_type', 'start_date', 'order']
    list_editable = ['order']
    list_filter = ['experience_type']
    ordering = ['order']
