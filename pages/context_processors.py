from .models import Developer
def developer(request):
    return {
        'dev': Developer.objects.get(id=1)
    }