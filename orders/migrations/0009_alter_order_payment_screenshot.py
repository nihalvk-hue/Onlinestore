# Generated by Django 5.1.6 on 2025-03-08 17:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_upi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_screenshot',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='payment_screenshots'),
        ),
    ]
