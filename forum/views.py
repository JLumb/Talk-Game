from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post
from .forms import RegistrationForm, PostForm


def RegisterPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, 'Profile successfully created for' + '' + user)
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
            return render(request, 'accounts/login.html', )
    context = {}
    
    return render(request, 'accounts/login.html', context)


def LogoutUser(request):

    logout(request)
    return redirect('home')


def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)


class postList(ListView):
    model = Post
    template_name = 'post_list.html'



@login_required(login_url='login')
def addPost(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(
                    request, 'Your post was created successfully!')
            return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/add_post.html', context)