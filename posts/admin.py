from django.contrib import admin

from posts.models import (
    Posts,
    Categories,
    Tags
)

# Register your models here.
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ('id', 'title', 'author', 'category', 'created_at',)
    list_display_links = ('id', 'title',)
    list_filter = ('tags', 'category',)
    search_fields = ['title',]



admin.site.register(Categories)
admin.site.register(Tags)
