from django.contrib import admin
from django.urls import path
from forum import views


urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('admin/', admin.site.urls),
    path('register', views.RegisterPage, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('add_post/', views.addPost, name='add_post'),
]