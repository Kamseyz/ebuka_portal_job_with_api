from django.urls import path
from .views import ViewJobs, DetailJobs, ApplicationView,PostJobs,EditJob,DeleteJob

urlpatterns = [
    #FRONT PAGE
    path('', ViewJobs.as_view(), name='view_jobs'),
    # TO POST JOBS BY EMPLOYERS ONLY
    path('create_job', PostJobs.as_view(), name='create_job'),
    #TO VIEW JOBS(EMPLOYERS ONLY)
    path('job_details/<int:pk>/', DetailJobs.as_view(), name='job_details'),
    # TO EDIT JOBS(EMPLOYERS ONLY)
    path('edit_job/<int:pk>/', EditJob.as_view(), name='edit_job'),
    # TO DELETE JOBS(EMPLOYER ONLY)
    path('delete_job/<int:pk>/', DeleteJob.as_view(), name='delete_job'),
    #TO VIEW APPLICATIONS(EMPLOYER ONLY)
    path('job_applications/<int:pk>/', ApplicationView.as_view(), name='job_applications'),
    

]
