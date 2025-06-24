from django import forms
from .models import Job



#JOB CREATION FORM FOR EMPLOYER
class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields =['title','responsibilities','status', 'qualifications','location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the job title'}),
            'responsibilites': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company address'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'qualifications': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What are the qualification you need?'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location of this job?'}),
        }
        labels = {
            'title': ' Job title',
            'responsibilite': 'Weytin be the qualification you need?',
            'status': 'Job status',
            'qualifications': 'Job qualifications',
            'location': 'Job location',
        }