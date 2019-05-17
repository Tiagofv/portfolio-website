from .models import Developer
def developer(request):
    return {
        'devs': Developer.objects.all().filter(id=1)
    }