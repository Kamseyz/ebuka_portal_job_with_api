from django import forms
from .models import WorkerDetails


class WorkerForm(forms.ModelForm):
    class Meta:
        model = WorkerDetails
        fields = ['name','phone_no', 'skills', 'upload_cv'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name in full'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone no'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fill in the type of skills you can do'}),
            'cv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Upload your cv'}),
    
        }
        labels = {
            'name': ' full_name',
            'phone_no': 'phone_no',
            'skills': 'skills',
            'cv': 'cv',
        }