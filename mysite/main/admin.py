from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import BlogCategory, Blogs, PhotoGallery, Calligraphy, CalliCategory


class BlogsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = ('title', 'pub_date')
    search_fields = ['content']

admin.site.register(BlogCategory)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(PhotoGallery)
admin.site.register(CalliCategory)
admin.site.register(Calligraphy)