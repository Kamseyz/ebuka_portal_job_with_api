from .views import WorkerRegisterView, EmployeeRegisterView, LoginUser, PostLoginRedirectView, DecisionPage,logout_view
from django.urls import path


urlpatterns = [
    #Register worker url
    path('register/worker/', WorkerRegisterView.as_view(), name='worker-register'),
    #Register employer url
    path('register/employer/', EmployeeRegisterView.as_view(), name='employer-register'),
    #login url for both employer and worker
    path('login/', LoginUser.as_view(), name='login'),
    #logout link for both employer and worker
    path('logout/', logout_view, name='logout'),
    #checks if the users(either worker and employer has filled the form after first login)
    path('after-login-check/', PostLoginRedirectView.as_view(), name='post-login-check'),
    #before registration it asks if they are a worker or an employer
    path('decisions/',DecisionPage.as_view(), name='decision_page' ),
]
