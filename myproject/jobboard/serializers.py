from rest_framework import serializers
from .models import Job,Application
from employers.serializer import SerializedEmployee
from workers.serializer import SerializedWorker



class SerializedJobs(serializers.ModelSerializer):
    posted_by = SerializedEmployee(read_only = True)
    class Meta:
        model = Job
        fields = '__all__'
        
        
class SerializedApplications(serializers.ModelSerializer):
    applicate = SerializedWorker(read_only = True)
    job = SerializedJobs(read_only=True)

    class Meta:
        model = Application
        fields = ['applicate', 'job' , 'status', 'date_applied']