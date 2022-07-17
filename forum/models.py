from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse


class Genre(models.Model):
    """  genre model so every post has a topic """
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Post(models.Model):
    """  Model for each post that is created """
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from=['title'])
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    
    
class Comment(models.Model):
    """ Model to comment on posts """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.content} by {self.author}"
