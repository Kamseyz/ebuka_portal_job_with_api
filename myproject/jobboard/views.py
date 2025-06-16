from django.views.generic import DetailView, ListView,CreateView
from .models import Job,Application
from django.urls import reverse_lazy
from .forms import JobCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#For website view

# TO VIEW JOBS
class ViewJobs(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10
    
    def get_queryset(self):
        return Job.objects.all().order_by('-created_at')


    
#TO POST JOBS
class PostJobs(LoginRequiredMixin,CreateView):
    form_class= JobCreationForm
    template_name= 'jobs/job_creation.html'
    success_url = reverse_lazy('view_jobs')
    
    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
        
    
    
    
    
#TO UPDATE JOBS

#TO DELETE JOBS



class DetailJobs(DetailView):
    model = Job
    template = 'jobs/job_details.html'
    context_object_name = 'job'
    
 
 

    
    
    
#FOR APPLICATION MODEL 
#FOR WEB

class ApplicationView(ListView):
    model = Application
    context_object_name = 'application_list'
    template_name = 'application/application_details.html'
    paginate_by = 5
    
 
 
