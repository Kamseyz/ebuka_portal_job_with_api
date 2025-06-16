from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SerializedWorker
from .models import WorkerDetails



# FOR MOBILE SIDE
#FOR API SIDE
class WorkerApi(APIView):
    def get(self, request):
        work = WorkerDetails.objects.all()
        serializer = SerializedWorker(work, many=True)
        return Response(serializer.data)
    
    def post(self, request):    
        serializer = SerializedWorker(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 201)
        return Response(serializer.errors, status= 400)