from rest_framework.views import APIView
from rest_framework import authentication, permissions
from .serializer import SerializedEmployee
from rest_framework.response import Response
from .models import Employee



#API EMPLOYEE VIEW

class EmployeeApi(APIView):
    authentication_classes = authentication
    permission_classes = permissions
    def get(self,request):
        employer = Employee.objects.all()
        serializer = SerializedEmployee(employer, many= True)
        return Response(serializer.data)