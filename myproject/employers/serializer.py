from .models import Employee
from rest_framework import serializers


class SerializedEmployee(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = '__all__'
        
        
        