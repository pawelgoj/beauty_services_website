# Generated by Django 4.1.7 on 2023-03-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_appointments_client_delete_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
