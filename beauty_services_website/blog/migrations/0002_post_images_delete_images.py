# Generated by Django 4.1.7 on 2023-03-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(to='blog.image'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
