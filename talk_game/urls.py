from django.contrib import admin
from django.urls import path, include
from forum import views


urlpatterns = [
    path('', views.LoginPage, name='login'),
    path('admin/', admin.site.urls),
    path('register', views.RegisterPage, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_post/', views.add_post, name='add_post'),
]