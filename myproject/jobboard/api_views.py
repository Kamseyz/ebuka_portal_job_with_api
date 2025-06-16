from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import SerializedJobs,SerializedApplications
from .models import Job,Application


#API FOR MOBILE VIEW or react or vue in the future
#TO SEE ALL THE JOBS AVAIABLE
class ApiJobs(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = SerializedJobs
    
    
    
#TO SEE A PARTICULAR JOB
class ApiJobsDetails(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = SerializedJobs
    
    
         
#API FOR THE APPLICATION MODEl 
# TO SEE ALL THE APPLICATION 
class ApiApplication(generics.ListAPIView):
    queryset =Application.objects.all()
    serializer_class=SerializedApplications
    permission_classes = [IsAuthenticated]