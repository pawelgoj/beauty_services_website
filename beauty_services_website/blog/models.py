from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    CONTENT_TYPES = [
        ('POST', 'Post'),
        ('Ogłoszenie', 'Ogłoszenie')
    ]
    content_type = models.CharField(choices=CONTENT_TYPES,
        default='Ogłoszenie', max_length=20)
    images = models.ManyToManyField("Image", blank=True)
    
    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(max_length=200)
    