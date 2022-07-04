from django.shortcuts import render
from django.views import generic
from .models import Post, Genre
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


def RegisterPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def LoginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
