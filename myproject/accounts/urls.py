from .views import WorkerRegisterView, EmployeeRegisterView, LoginUser, LogoutUser, AfterLoginCheck, DecisionPage
from django.urls import path


urlpatterns = [
    path('register/worker/', WorkerRegisterView.as_view(), name='worker-register'),
    path('register/employer/', EmployeeRegisterView.as_view(), name='employer-register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('after-login-check/', AfterLoginCheck.as_view(), name='after-login-check'),
    path('decisions/',DecisionPage.as_view(), name='decision_page' )
]
