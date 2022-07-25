from django.shortcuts import render
from Portfolio.models import Project

def home(request):
    project = Project.objects.all()
    return render(request, 'Portfolio/home.html',{'project':project})
    
