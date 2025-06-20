from .views import WorkerRegisterView, EmployeeRegisterView, LoginUser, PostLoginRedirectView, DecisionPage,logout_view
from django.urls import path


urlpatterns = [
    path('register/worker/', WorkerRegisterView.as_view(), name='worker-register'),
    path('register/employer/', EmployeeRegisterView.as_view(), name='employer-register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('after-login-check/', PostLoginRedirectView.as_view(), name='post-login-check'),
    path('decisions/',DecisionPage.as_view(), name='decision_page' ),
]
