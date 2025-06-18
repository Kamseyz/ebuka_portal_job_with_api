from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


# Employee information model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employeedetails')
    company_name =models.CharField(blank= False, null= False, max_length=100)
    company_address =models.CharField(blank= False, null = False, max_length=250)
    company_phone_no =models.CharField(blank= False, null= False, max_length=20)
    no_of_employees =models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.company_name