from django.contrib import admin
from .models import Post, Comment, Genre, Video


@admin.register(Genre)
@admin.register(Post)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('author', 'email', 'body', 'created')

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

