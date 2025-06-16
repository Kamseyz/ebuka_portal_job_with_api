from django.urls import path
from .api_views import ApiJobs,ApiApplication, ApiJobsDetails

urlpatterns = [
    path('api_jobs/', ApiJobs.as_view(), name= 'mobile-jobs'),
    path('api_jobs/<int:pk>', ApiJobsDetails.as_view(), name= 'mobile-jobs'),
    path('api_application/', ApiApplication.as_view(), name='jobs-application')
]



