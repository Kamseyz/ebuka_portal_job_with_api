from django.urls import path
from .views import ViewJobs, DetailJobs, ApplicationView

urlpatterns = [
    path('', ViewJobs.as_view(), name='view_jobs'),
    path('job_details/<int:pk>', DetailJobs.as_view(), name='job_details'),
    path('job_applications', ApplicationView.as_view(), name='job_application')
]
