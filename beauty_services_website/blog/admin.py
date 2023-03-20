from django.contrib import admin
from .models import Post, Image

# możemy dodaćkolumny które widzi administrator 
#dekorator do rejstrowania danej tabeli 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content_type')
    search_fields = ['title', 'date', 'content_type']
    ordering = ('title', 'date')
    list_filter = ('title', 'date', 'content_type')

# Register your models here.

admin.site.register(Image)
