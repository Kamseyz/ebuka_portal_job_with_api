from .forms import EmployeeRegistrationForm, WorkerRegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from allauth.account.utils import send_email_confirmation

#EMPLOYER REGISTER VIEW
class EmployeeRegisterView(CreateView):
    form_class = EmployeeRegistrationForm
    template_name = 'account/registeremployeer.html'
    success_url = reverse_lazy('after-login-check')
    
    def form_valid(self, form):
        user = form.save()
        user.user_type = 'employer'
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        send_email_confirmation(self.request, user)
        messages.success(self.request, 'Employee account was created successfully')
        return redirect('after-login-check')
    

#WORKERS REGISTER VIEW
class WorkerRegisterView(CreateView):
    form_class = WorkerRegistrationForm
    template_name = 'account/registerworkers.html'
    success_url = reverse_lazy('after-login-check')
    
    def form_valid(self, form):
        user = form.save()
        user.user_type = 'worker'
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        send_email_confirmation(self.request, user)
        messages.success(self.request, 'Account was created successfully')
        return redirect('after-login-check')
    


#LOGIN VIEW
class LoginUser(LoginView):
    authentication_form = LoginForm
    template_name = 'account/login.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Welcome back')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid credential, try again!')
        return super().form_invalid(form)
        

#LOGOUT USER 
class LogoutUser(LogoutView):
    next_page = reverse_lazy('login')
    
    
#AFTER LOGIN CHECK THE USER 

class AfterLoginCheck(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    def get(self, request, *args, **kwargs):
        user = request.user
        
        if not user.is_authenticated:
            return redirect('login')
        
        # check if the user have filled the required form
        if user.user_type == 'worker':
            # Check if worker has completed profile
            has_worker_details = hasattr(user, 'workerdetails')
            return redirect('worker-dashboard' if has_worker_details else 'worker-complete-profile')
        
        elif user.user_type == 'employer':
            # Check if employer has completed profile
            has_employee_details = hasattr(user, 'employee')
            return redirect('employee-dashboard' if has_employee_details else 'employee-complete-profile')
        
        # If user_type doesn't match, redirect to login or show error
        messages.error(request, 'Invalid user type')
        return redirect('login')
    
    
    
class DecisionPage(TemplateView):
    template_name = 'account/decision.html'