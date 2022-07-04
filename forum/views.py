from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Genre
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout


def RegisterPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, 'Profile successfully created for' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def LoginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
