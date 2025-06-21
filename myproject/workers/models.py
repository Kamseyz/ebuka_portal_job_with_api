from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
# Create your models here.


User = get_user_model()

class WorkerDetails(models.Model):
    class StatusChoice(models.TextChoices):
        AVAILABLE ='available', 'Available'
        EMPLOYED = 'employed', 'Employed'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='workerdetails')
    name = models.CharField(max_length=100, blank= False, null= False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",)
    phone_no = models.CharField(validators=[phone_regex],max_length=15, blank= False, null=False, default='')
    skills= models.CharField(max_length=100, blank= False, null= False)
    status=models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.AVAILABLE)
    upload_cv = models.FileField(upload_to='cv/', null= True, blank= True)
    created_at= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name