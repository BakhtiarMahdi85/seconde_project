from django.contrib import admin

from .models import Blog_Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)

admin.site.register(Blog_Post, PostAdmin)

