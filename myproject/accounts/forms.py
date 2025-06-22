from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Users


User = get_user_model()

#BASE REGISTRATION FORM
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter your email address pls', 
                             widget=forms.TextInput(attrs={'class':'form-control'}))
    
    user_type = forms.ChoiceField(choices=Users.UserType.choices
                                  ,widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['email', 'user_type', 'password1', 'password2']
    
    
    #GET CLEAN EMAIL AND CHECK IF ALREADY EXIST
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise ValidationError('Email already exist')
        return email
    
    
    #SAVE CLEAN EMAIL AND USER TYPE 
    def save(self, commit = True):
        user = super().save(commit = False) 
        if commit:
            user.save()
        return user
   
    
#WORKER REGISTRATION FORM + BASE REGISTRATION
class WorkerRegistrationForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('user_type')
        
    def save(self, commit=True):
        user = super().save(commit = False)
        if commit:
            user.save()
        return user


#EMPLOYEE REGISTRATION FORM + BASE REGISTRATION
class EmployeeRegistrationForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('user_type')
        
    def save(self, commit=True):
        user = super().save(commit = False)
        if commit:
            user.save()
        return user


#LOGIN FORM
class LoginForm(AuthenticationForm):
    username = forms.EmailField(required= True, 
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter email address', 'class':'form-control'}))
    password = forms.CharField(required= True, 
                             widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class':'form-control'}))