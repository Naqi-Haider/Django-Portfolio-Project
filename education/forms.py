from django import forms
from .models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_year', 'end_year', 'description', 'order']
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-input'}),
            'institution': forms.TextInput(attrs={'class': 'form-input'}),
            'start_year': forms.TextInput(attrs={'class': 'form-input'}),
            'end_year': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'order': forms.NumberInput(attrs={'class': 'form-input'}),
        }
