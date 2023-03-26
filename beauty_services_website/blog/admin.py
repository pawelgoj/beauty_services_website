import logging
from django.contrib import admin
from .models import Post, Image
from django.utils.html import mark_safe


# możemy dodaćkolumny które widzi administrator 
#dekorator do rejstrowania danej tabeli 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_img']
    list_display = ('title', 'date', 'content_type')
    search_fields = ['title', 'date', 'content_type']
    ordering = ('title', 'date')
    list_filter = ('title', 'date', 'content_type')
    
    def preview_img(self, obj):
        
        images = obj.images.values()
        html = ""
        for image in images:
            id = image.get('id')
            image_object = Image.objects.get(id=id)
            html += f' <img src = "{image_object.image.url}" width = "300"/> '

        return mark_safe(html)


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ('name',)



