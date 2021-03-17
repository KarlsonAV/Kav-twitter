from django.contrib import admin
from .models import Post, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment


class PostsAdmin(admin.ModelAdmin):
    inlines = [
        CommentsInLine,
    ]
    list_display = ('author', 'content')


admin.site.register(Post, PostsAdmin)