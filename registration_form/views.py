from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registration_form(request):
    return render(request, 'registration.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})
