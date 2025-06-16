from django import forms
from .models import WorkerDetails


class WorkerForm(forms.ModelForm):
    class Meta:
        model = WorkerDetails
        fields = ['name', 'email','skills'] 