from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.


def home(request):
    teachers = {'teachers': ['Alex', 'Tao', 'Jake', 'Nafis']}
    return render(request, 'home.html', context=teachers)


def projects(request):
    return HttpResponse("This is my projects page! (projects/)")


# class base view
class contact(View):
    def get(self, request):
        return render(request, 'contact.html')
