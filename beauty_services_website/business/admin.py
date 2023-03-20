from django.contrib import admin
from .models import Service, Contact, SocialMedia, Clients

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
    
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name',)

