# Generated by Django 5.1.6 on 2025-03-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_fill_order_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='alt_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
