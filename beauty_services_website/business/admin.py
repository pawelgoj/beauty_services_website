from django.contrib import admin
from .models import Service, Contact, SocialMedia, Client, Appointment

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

