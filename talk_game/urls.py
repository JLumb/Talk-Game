"""talk_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forum import views


urlpatterns = [
    path('', views.LoginPage, name='login'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('register', views.RegisterPage, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('battle_royale/', views.battle_royale, name='battle_royale'),
    path('sports/', views.sports, name='sports'),
    path('mmorpg/', views.mmorpg, name='mmorpg'),
    path('fps/', views.fps, name='fps'),

]