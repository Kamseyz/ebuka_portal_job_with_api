from rest_framework import serializers
from .models import WorkerDetails


class SerializedWorker(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails 
        fields = '__all__'
        
        