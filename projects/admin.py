from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'technologies', 'order']
    list_editable = ['order']
    list_filter = ['project_type']
    ordering = ['order']
