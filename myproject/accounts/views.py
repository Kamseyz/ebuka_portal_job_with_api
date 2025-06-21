from .forms import EmployeeRegistrationForm, WorkerRegistrationForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView,View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from allauth.account.utils import send_email_confirmation

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

#EMPLOYER REGISTER VIEW
class EmployeeRegisterView(CreateView):
    form_class = EmployeeRegistrationForm
    template_name = 'account/registeremployeer.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'employer'
        user.save()
        send_email_confirmation(self.request, user)
        messages.success(self.request, 'Employee account was created successfully')
        return redirect('login')
    

#WORKERS REGISTER VIEW
class WorkerRegisterView(CreateView):
    form_class = WorkerRegistrationForm
    template_name = 'account/registerworkers.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'worker'
        user.save()
        send_email_confirmation(self.request, user)
        messages.success(self.request, 'Account was created successfully')
        return redirect('login')
    


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
@login_required
def logout_view(request):
    logout(request)
    return redirect('view_jobs')
    
    
#AFTER LOGIN CHECK THE USER 
class PostLoginRedirectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user

        if user.user_type == 'worker':
            if not hasattr(user, 'workerdetails'):
                return redirect('worker_creation_profile')
            return redirect('view_jobs')

        elif user.user_type == 'employer':
            if not hasattr(user, 'employeedetails'):
                return redirect('employee-dashboard')
            return redirect('employee-dashboard-view')

        return redirect('home')

class DecisionPage(TemplateView):
    template_name = 'account/decision.html'
    
    
