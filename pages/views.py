from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Projects, Developer, Education, Work
# Create your views here.
def index(req):
    portfolio = Projects.objects.all()
    developer = Developer.objects.filter(id=1)
    education = Education.objects.all().order_by('-begin_date')
    work = Work.objects.all().order_by('-hire_date')
    context = {
        'portfolio': portfolio,
        'devs': developer,
        'education': education,
        'work': work
    }
    return render(req, 'index.html', context)

def projects(req, id):
    project = get_object_or_404(Projects, pk = id)
    context = {
        'project': project
    }
    return render(req, 'project.html', context)