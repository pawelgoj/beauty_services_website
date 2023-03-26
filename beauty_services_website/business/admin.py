from typing import Any
from django.contrib import admin
from .models import Service, Contact, SocialMedia, Client, Appointment, AboutMe
from django.http.request import HttpRequest
from django.db.models.base import Model


# Register your models here.
# możemy dodaćkolumny które widzi administrator 
#dekorator do rejstrowania danej tabeli 
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Appointment)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'date')


@admin.register(AboutMe)
class ClientAdmin(admin.ModelAdmin):
    """Only one recort AboutMe must exist"""
    #The admin have not remove button
    readonly_fields = ['img_preview']
    def has_delete_permission(self, request: HttpRequest, obj: Model=None) -> bool:
        return False
    
    def save_model(self, request: Any, obj: Model, form: Any, change: Any) -> None:
        #only one record of About me
        if obj.aboutme_id == 1:
            super().save_model(request, obj, form, change)
        else:
            # Search object of primary key:
            AboutMe.objects.filter(aboutme_id=1).update(text=obj.text, image=obj.image)

