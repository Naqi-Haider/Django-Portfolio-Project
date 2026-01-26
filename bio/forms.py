from django import forms
from .models import Bio

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['name', 'job_title', 'description', 'profile_picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'job_title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'profile_picture': forms.URLInput(attrs={'class': 'form-input'}),
        }
