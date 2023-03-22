from django.contrib import admin
from .models import ImageForGallery


# Register your models here.
@admin.register(ImageForGallery)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)