from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import RegistrationForm, PostForm
from django.urls import reverse_lazy


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
    return render(request, 'accounts/home.html')


class postList(ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 6


class postView(DetailView):
    model = Post
    template_name = 'post_view.html'


def postLike(request, pk):

    post = Post.objects.get(id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_view', args=[str(pk)]))


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


class editPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'genre', 'content']


class deletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'search_results.html', {'searched': searched})
    else:
        return render(request, 'search_results.html', {})
