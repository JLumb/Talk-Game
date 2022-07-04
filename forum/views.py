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

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    
    return render(request, 'accounts/login.html', context)


def LogoutUser(request):

    logout(request)   
    return redirect('login')


def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)
