from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField


class Post(models.Model):
    """  Model for each post that is created """
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from=['title'])
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class Video(models.Model):
    title = models.CharField(max_length=50)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)


class Genre(models.Model):
    genre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.genre


class Comment(models.Model):
    """ Model to comment on posts """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
