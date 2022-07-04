from django import forms
from .models import Post, Genre


genre_choices = Genre.objects.all().values_list('genre','genre')

genre_list = []

for item in genre_choices:
    genre_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'genre', 'body')

        items = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'genre': forms.Select(choices=genre_list, attrs={
                'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),


        }