from django.contrib import admin
from .models import Profile, Education, Skill, Experience

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'institution', 'date_range', 'order']
    list_editable = ['order']
    ordering = ['order']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'date', 'order']
    list_editable = ['order']
    ordering = ['order']
