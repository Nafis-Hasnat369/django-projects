from django.shortcuts import render
from about.forms import TeachersRegistration
from about.models import Teacher


# Create your views here.
def about(request):
    return render(request, 'about.html')


def teachers_info(request):
    teacher = Teacher.objects.all()
    return render(request, 't.html', {'teacher': teacher})


def show_forms_data(request):
    form = TeachersRegistration()
    form.order_fields(field_order=['email', 'last_name', 'first_name'])
    return render(request, 'forms.html', {'form': form})
