
from django.contrib import admin

from blog.models import Image
from .models import ImageForGallery
from django.utils.html import mark_safe

# Register your models here.
@admin.register(ImageForGallery)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_img']
    list_display = ('name',)
    
    def preview_img(self, obj):
        
        id = obj.image.id
        image_object = Image.objects.get(id=id)
        return mark_safe(f'<img src = "{image_object.image.url}" width = "300"/>')

    