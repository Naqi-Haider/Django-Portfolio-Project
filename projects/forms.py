from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'project_type', 'technologies', 'description', 'github_link', 'live_link', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'project_type': forms.Select(attrs={'class': 'form-input'}),
            'technologies': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'github_link': forms.URLInput(attrs={'class': 'form-input'}),
            'live_link': forms.URLInput(attrs={'class': 'form-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-input'}),
        }
