from django.contrib import admin
from django.urls import path
from forum import views
from forum.views import postList, postView


urlpatterns = [

    path('', views.home, name='home'),
    path('post_list/', postList.as_view(), name='post_list'),
    path('login/', views.LoginPage, name='login'),
    path('admin/', admin.site.urls),
    path('register', views.RegisterPage, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('add_post/', views.addPost, name='add_post'),
    path('post_view/<int:pk>', postView.as_view(), name='post_view'),
    
]