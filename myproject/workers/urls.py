from django.urls import path
from .views import WorkerCreationProfile,WorkerProfile,WorkerUpdate,WorkerDelete,UploadCVView

urlpatterns = [
    #create worker profile
    path('worker_profile/', WorkerCreationProfile.as_view(), name='worker_creation_profile'),
        #View worker profile
    path('worker_info/<int:pk>/', WorkerProfile.as_view(), name='worker_info'),
        #Update worker profile
    path('update_worker_info/<int:pk>/', WorkerUpdate.as_view(), name='worker_update'),
        #Delete worker profile
    path('delete_worker_info/<int:pk>',WorkerDelete.as_view(), name='worker_deletation'),
    # UPLOAD CV
    path('upload_cv/<int:pk>/', UploadCVView.as_view(), name='upload_cv'),
]
