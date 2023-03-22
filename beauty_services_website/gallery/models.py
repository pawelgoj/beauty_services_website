from django.db import models
from blog.models import Image

# Create your models here.

class ImageForGallery(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tytuł")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name="Obrazek")
    text = models.TextField(verbose_name="Tekst")
    
    class Meta:
        verbose_name_plural = "Obrazki w galerii"
        verbose_name = "Obrazek"
