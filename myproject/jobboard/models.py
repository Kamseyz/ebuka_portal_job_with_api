from django.db import models
from employers.models import Employee
from workers.models import WorkerDetails
# Create your models here.


#POV Later link to the employee model

#Job model
class Job(models.Model):
    class Choices(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        NOT_AVAILABLE = 'not_available', 'Not Available'
        
    title = models.CharField(max_length=100, null=False, blank= False)
    posted_by = models.ForeignKey(Employee,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Choices.choices, default=Choices.AVAILABLE)
    responsibilities = models.TextField(max_length=300, null= False, blank= False, default="")
    qualifications = models.CharField(max_length=100, null= False, blank= False)
    
    def __str__(self):
        return self.title
    
    
    
#Application model
class Application(models.Model):
    class Application_status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACCEPTED = 'accepted', 'Accepted'
        REJECTED = 'rejected', 'Rejected'
    applicate = models.ForeignKey(WorkerDetails, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Application_status.choices, default=Application_status.PENDING)
    
    
    def __str__(self):
        return f'{self.applicate} applied for a role in {self.job}'