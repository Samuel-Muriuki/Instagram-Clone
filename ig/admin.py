from django.contrib import admin

from ig.models import Comment, Post, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
