from django.contrib import admin
from .models import Post, PostImage, Category, Tag


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class PostInline(admin.TabularInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [PostInline, ]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
