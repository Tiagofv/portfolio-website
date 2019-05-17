from django.shortcuts import render
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