from django.db import models
from django.utils.html import mark_safe


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    date = models.DateField(auto_now=True, verbose_name="Data")
    content = models.TextField(verbose_name="Treść")
    CONTENT_TYPES = [
        ('Post', 'Post'),
        ('Ogłoszenie', 'Ogłoszenie')
    ]
    content_type = models.CharField(choices=CONTENT_TYPES,
        default='Ogłoszenie', max_length=20, verbose_name="Typ")
    images = models.ManyToManyField("Image", blank=True, verbose_name="Obrazek")


    class Meta:
        verbose_name_plural = "Posty"
        verbose_name = "Post"
    
    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(max_length=200, verbose_name="Obrazek")
    name = models.CharField(max_length=200, verbose_name="Nazwa", default="Img")
    
    class Meta:
        verbose_name_plural = "Obrazki"
        verbose_name = "Obrazek"
    
    def img_preview(self):
        # Kod do pokazania obrazka
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
    