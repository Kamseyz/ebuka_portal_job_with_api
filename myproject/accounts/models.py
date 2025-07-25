from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#DELETE THIS BEFORE PUSHING TO PRODUCTION 
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


#######DELETE THE ABOVE CODE

#USER TYPE AND REGISTRATION USERNAME NONE, WITH EMAIL, PROFILE PICTURE, AND USER TYPE
class Users(AbstractUser):
    class UserType(models.TextChoices):
        WORKER = 'worker', 'Worker'
        EMPLOYER = 'employer', 'Employer'
        
    username = None
    email = models.EmailField(unique=True, blank= False, null= False, max_length=100)
    profile_img = models.ImageField(upload_to= 'images/', blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=UserType.choices)
        
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
      # ✅ use your custom manager DELETE THIS TOO ALSO 
    objects = CustomUserManager()
    
    #THE ABOVE OBJECT DELETE IT AND MAKE MIGRATION AFTER YOU ARE DONE 
    
    
    def __str__(self):
        return f'The account {self.email} is a {self.user_type}'
        
    