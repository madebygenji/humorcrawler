from django.contrib import admin
from .models import Post, PostImage



class PostInline(admin.TabularInline):
    model = PostImage
    

class PostAdmin(admin.ModelAdmin):
    inlines = [PostInline, ]


# Register your models here.
admin.site.register(Post, PostAdmin)