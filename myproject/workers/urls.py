from django.urls import path
from .views import Worker,WorkerProfile,WorkerUpdate,WorkerDelete

urlpatterns = [
    #create worker profile
    path('worker_profile/', Worker.as_view(), name='worker_dashboard'),
        #View worker profile
    path('worker_info/', WorkerProfile.as_view(), name='worker_info'),
        #Update worker profile
    path('update_worker_info/<int:pk>/', WorkerUpdate.as_view(), name='worker_update'),
        #Delete worker profile
    path('delete_worker_info/<int:pk>',WorkerDelete.as_view(), name='worker_deletation'),
]
