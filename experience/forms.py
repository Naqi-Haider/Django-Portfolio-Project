from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'organization', 'experience_type', 'start_date', 'end_date', 'description', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'organization': forms.TextInput(attrs={'class': 'form-input'}),
            'experience_type': forms.Select(attrs={'class': 'form-input'}),
            'start_date': forms.TextInput(attrs={'class': 'form-input'}),
            'end_date': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'order': forms.NumberInput(attrs={'class': 'form-input'}),
        }
