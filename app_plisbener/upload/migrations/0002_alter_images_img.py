# Generated by Django 4.2.1 on 2023-05-29 21:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]