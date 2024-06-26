from django.shortcuts import render
from about.models import Teacher


# Create your views here.
def about(request):
    return render(request, 'about.html')


def teachers_info(request):
    teacher = Teacher.objects.all()
    return render(request, 't.html', {'teacher': teacher})
