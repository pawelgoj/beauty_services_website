from django.db import models

# Create your models here.

class Service(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    
    class Meta:
        ordering =('name',)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    
class Appointments(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    place = models.CharField(max_length=200)
    description = models.TextField(blank=True)