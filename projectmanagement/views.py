from django.shortcuts import render

from projectmanagement.models import Project
from .models import Project
# Create your views here.

def index(request):
    projects = Project.objects.all()
    completed = Project.objects.filter(status='b')
    ongoing = Project.objects.filter(status='a')
    stalled = Project.objects.filter(status='c')
    return render(request,'projectmanagement/index.html',{'projects':projects,
                                                            'completed':completed,
                                                            'ongoing':ongoing,
                                                            'stalled':stalled,})
