from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()[:10]
    return render(request, 'listings/job_list.html', {'jobs': jobs})

# Create your views here.
