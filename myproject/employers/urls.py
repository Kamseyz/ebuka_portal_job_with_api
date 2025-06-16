from django.urls import path
from .views import EmployeeView,EmployeeDetails, UpdateEmployeeInfo,DeleteEmployeeInfo,EmployeeDashboard

urlpatterns = [
    # This handles profile creation
    path('employee_dashboard/', EmployeeView.as_view(), name='employee-dashboard'),
    # This shows the actual dashboard
    path('dashboard/', EmployeeDashboard.as_view(), name='employee-dashboard-view'),
    # View profile employee
    path('employee_info/', EmployeeDetails.as_view(), name='employee-info'),
    # Update employee profile
    path('employee_update_info/<int:pk>/', UpdateEmployeeInfo.as_view(), name='employee-update-info'),
    # Delete employee
    path('employee_delete_info/<int:pk>/', DeleteEmployeeInfo.as_view(), name='employee-delete-info'),
]

