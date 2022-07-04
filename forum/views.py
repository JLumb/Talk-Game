from django.shortcuts import render
from django.views import generic
from .models import Post, Genre
from django.contrib.auth.forms import UserCreationForm


def RegisterPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def LoginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
