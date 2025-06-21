from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from .models import WorkerDetails
from .forms import WorkerForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.


#WEBSITE MODEL

#TO CREATE PROFILE FOR WORKER AS A FIRST TIMER WHEN THEY LOGIN
class WorkerCreationProfile(LoginRequiredMixin,CreateView):
    template_name = 'workers/worker_creation.html'
    model = WorkerDetails
    form_class = WorkerForm
    context_object_name = 'workers'
    success_url = reverse_lazy('view_jobs')
    
#CHECK IF PROFILE ALREADY EXIST
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user ,'workerdetails'):
            return redirect('view_jobs')
        return super().dispatch(request, *args, **kwargs)
    

#Check if form is valid
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Account was created successfully')
        return super().form_valid(form)
    
    
    
# UPLOAD CV CODE
from django.http import HttpResponseRedirect

class UploadCVView(LoginRequiredMixin, UpdateView):
    model = WorkerDetails
    fields = ['upload_cv']
    template_name = None  # We don't want to render any template

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))

    def form_invalid(self, form):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))

    def get_queryset(self):
        return WorkerDetails.objects.filter(user=self.request.user)


#Read worker profile
class WorkerProfile(LoginRequiredMixin,DetailView):
    model =WorkerDetails
    context_object_name = 'workers'
    template_name = 'workers/worker_profile.html'
    

   

#Update Worker profile

class WorkerUpdate(LoginRequiredMixin,UpdateView):
    model =WorkerDetails
    form_class = WorkerForm
    context_object_name = 'workers'
    template_name = 'workers/worker_update.html'
    success_url = reverse_lazy('worker_dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,'Account was updated successfully')
        return super().form_valid(form)
    
    def get_queryset(self):
        return WorkerDetails.objects.filter(user = self.request.user)
#Delete Worker Profile

class WorkerDelete(LoginRequiredMixin, DeleteView):
    model =WorkerDetails
    template_name = 'workers/worker_deletation.html'
    success_url=reverse_lazy('login')
    
    def get_queryset(self):
        messages.error(self.request, 'Account was deleted successfully')
        return WorkerDetails.objects.filter(user= self.request.user)
    