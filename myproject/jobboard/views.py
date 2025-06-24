from django.views.generic import DetailView, ListView,CreateView,UpdateView,DeleteView,View
from .models import Job,Application
from django.urls import reverse_lazy
from .forms import JobCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

#For website view

# TO VIEW JOBs BOTH FOR WORKERS AND EMPLOYERS
class ViewJobs(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10
    
    def get_queryset(self):
        return Job.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        is_worker = False
        worker_pk = None

        if user.is_authenticated:
            try:
                worker_profile = user.workerdetails
                is_worker = True
                worker_pk = worker_profile.pk
            except:
                pass

        context['is_worker'] = is_worker
        context['worker_pk'] = worker_pk
        return context


    
#TO ADD/POST JOBS ONLY FOR EMPLOYERS
class PostJobs(LoginRequiredMixin,CreateView):
    form_class= JobCreationForm
    template_name= 'jobs/job_creation.html'
    success_url = reverse_lazy('employee-dashboard-view')
    
    def form_valid(self, form):
        form.instance.posted_by = self.request.user.employeedetails
        messages.success(self.request, 'You job as been posted')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid form submission')
        return super().form_invalid(form)
    
    
#TO EDIT JOB (EMPLOYERS ONLY)
class EditJob(LoginRequiredMixin,UpdateView):
    model = Job
    fields = ['title','responsibilities','status', 'qualifications','location']
    template_name = 'jobs/job_edit.html'
    context_object_name = 'job'
    
    
    def get_queryset(self):
        return Job.objects.filter(posted_by = self.request.user.employeedetails)
    
    def get_success_url(self):
        return reverse_lazy('employee-dashboard-view')
    
     
#TO DELETE JOB (EMPLOYERS ONLY)
class DeleteJob(LoginRequiredMixin,DeleteView):
    model = Job
    template_name= 'jobs/confirm_delete.html'
    success_url = reverse_lazy('employee-dashboard-view')
    
    
    def get_queryset(self):
        return Job.objects.filter(posted_by = self.request.user.employeedetails)
    
    
#TO GET MORE DETAILS OF THE JOB
class DetailJobs(LoginRequiredMixin,DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'   
    

#Apply for job(workers only)
class ApplyJob(LoginRequiredMixin, View):  
    def post(self, request, pk, *args, **kwargs):
        job = get_object_or_404(Job, pk=pk)

        # Check if user is a worker
        if not hasattr(request.user, 'workerdetails'):
            messages.error(request, "Only workers can apply for jobs.")
            return redirect('job_details', pk=pk)

        worker = request.user.workerdetails

        # Check if already applied
        if Application.objects.filter(applicate=worker, job=job).exists():
            messages.info(request, "You have already applied for this job.")
        else:
            Application.objects.create(applicate=worker, job=job)
            messages.success(request, "Application submitted successfully!")

        return redirect('job_details', pk=pk)


#SEE WHO APPLIED(WORKER)
class ApplicationView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'application/application_details.html'
    context_object_name = 'jobs'
    
    def get_queryset(self):
        return Job.objects.filter(posted_by = self.request.user.employeedetails)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        context['applications'] = Application.objects.filter(job=job).select_related('applicate')
        return context
    
#TO UPDATE JOBS

#TO DELETE JOBS



    
 
 

    
    
    
#FOR APPLICATION MODEL 
#FOR WEB

