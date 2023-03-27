from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Service(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Cena")
    name = models.CharField(max_length=100, verbose_name="Nazwa")
    short_description = models.CharField(max_length=200, verbose_name="Krótki opis")
    long_description = models.TextField(verbose_name="Długi opis")
    
    class Meta:
        ordering =('name',)
        verbose_name_plural = "Usługi"
        verbose_name = "Usługa"

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nick")
    email = models.EmailField(max_length=100, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Numer telefonu")
    question = models.CharField(max_length=500, verbose_name="Zapytanie")

    class Meta:
        verbose_name_plural = "Zapytania"
        verbose_name = "Zapytanie"

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa")
    link = models.CharField(max_length=200, verbose_name="Link")
    CONTENT_TYPES = [
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Tiktok', 'Tiktok'),
        ('Pinterest', 'Pinterest')
    ]
    logo = models.CharField(choices=CONTENT_TYPES,
        default='Instagram', max_length=20, verbose_name="Logo")

    description = models.CharField(max_length=200, verbose_name="Opis")

    class Meta:
        verbose_name_plural = "Moje socialmedia"
        verbose_name = "Socialmedia"

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Nazwisko")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Numer telefonu")
    email = models.EmailField(max_length=100, blank=True, verbose_name="Email")
    description = models.CharField(max_length=500, blank=True, verbose_name="Uwagi")
    active = models.BooleanField(default=True, verbose_name="Aktywny klient")

    class Meta:
        verbose_name_plural = "Klienci"
        verbose_name = "Klient"

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False, verbose_name="Data")
    place = models.CharField(max_length=200, verbose_name="Miejsce")
    description = models.TextField(blank=True, verbose_name="Opis")

    class Meta:
        verbose_name_plural = "Terminy umówione"
        verbose_name = "Termin"
        
        
class AboutMe(models.Model):
    aboutme_id = models.AutoField(primary_key=True)

    # Upload_to is not necessary because in setting was chosen folder with media. 
    image = models.ImageField(max_length=200, verbose_name="Moje zdjęcie", blank=True, upload_to = 'media')
    text = models.TextField(verbose_name="Opis")

    # to show image in administration panel
    def img_preview(self):
        #KKod do pokazania obrazka
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

    class Meta:
        verbose_name_plural = "O mnie"
        verbose_name = "O mnie"
        constraints = [
            models.CheckConstraint(check=models.Q(aboutme_id=1), name='one instance'),
        ]

    def __str__(self):
        return 'O mnie'