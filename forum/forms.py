from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Genre


genre_choices = Genre.objects.all().values_list('genre', 'genre')

genre_list = []

for item in genre_choices:
    genre_list.append(item)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

