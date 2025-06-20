from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['company_name', 'company_address', 'company_phone_no', 'no_of_employees']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company address'}),
            'company_phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company phone number'}),
            'no_of_employees': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How many employees?'}),
        }
        labels = {
            'company_name': 'Company Name',
            'company_address': 'Company Address',
            'company_phone_no': 'Company Phone Number',
            'no_of_employees': 'Number of Employees',
        }
        