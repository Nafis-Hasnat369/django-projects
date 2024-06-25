from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    teachers = {'teachers': ['Alex', 'Tao', 'Jake', 'Nafis']}
    return render(request, 'home.html', context=teachers)


def about(request):
    return HttpResponse("This is my about page! (about/)")


def projects(request):
    return HttpResponse("This is my projects page! (projects/)")


def contact(request):
    return HttpResponse("This is my contact page! (contact/)")
