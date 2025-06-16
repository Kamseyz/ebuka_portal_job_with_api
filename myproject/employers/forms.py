from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['company_name', 'company_address', 'company_phone_no', 'no_of_employees']
        