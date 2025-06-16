from .models import Employee
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from jobboard.models import Job

# EMPLOYEE PROFILE CREATION
class EmployeeView(LoginRequiredMixin, CreateView):
    form_class = EmployeeForm
    template_name = 'employee/employee_creation.html'
    model = Employee
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-dashboard-view') 
    
    # Check if profile already exists
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'employee'):
            return redirect('employee-dashboard-view')
        return super().dispatch(request, *args, **kwargs)
    
    # Check form is valid
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Employer profile created successfully!')
        return super().form_valid(form)

# EMPLOYEE DASHBOARD
class EmployeeDashboard(LoginRequiredMixin, TemplateView): 
    template_name = 'employee/employee_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = self.request.user.employee
        context['jobs'] = Job.objects.filter(posted_by=self.request.user.employee)
        context['total_jobs'] = context['jobs'].count()
        context['available_jobs'] = context['jobs'].filter(status='available').count()
        return context

# SHOW EMPLOYEE DETAILS
class EmployeeDetails(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee/employee_info.html'
    context_object_name = 'employee'
    
    def get_object(self):
        return self.request.user.employee
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(posted_by=self.request.user.employee)
        return context

# UPDATE EMPLOYEE FORM
class UpdateEmployeeInfo(LoginRequiredMixin, UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'employee/update_employee.html'  
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-dashboard-view')  
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Account was updated successfully')
        return super().form_valid(form)
    
    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)

# DELETE EMPLOYEE FORM
class DeleteEmployeeInfo(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'  
    success_url = reverse_lazy('login')  
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Account was deleted successfully') 
        return super().delete(request, *args, **kwargs)
    
    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)