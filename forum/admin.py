from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment,  Genre


@admin.register(Genre)
@admin.register(Post)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('author', 'email', 'body', 'created')

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

