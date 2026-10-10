from django import forms
from .models import ResumeModel

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Short personal objective'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institute_name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_graduation': forms.NumberInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Python, Django, HTML (comma-separated)'}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'achievements': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }