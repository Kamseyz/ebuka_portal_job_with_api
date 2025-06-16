from django.urls import path
from .api_views import WorkerApi

urlpatterns = [
    path('api_worker/', WorkerApi.as_view(), name= 'workers'),
]



