from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class WorkerDetails(models.Model):
    class StatusChoice(models.TextChoices):
        AVAILABLE ='available', 'Available'
        EMPLOYED = 'employed', 'Employed'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='workerdetails')
    name = models.CharField(max_length=100, blank= False, null= False)
    email = models.EmailField(max_length=100, blank= False, null=False)
    skills= models.CharField(max_length=100, blank= False, null= False)
    status=models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.AVAILABLE)
    created_at= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name