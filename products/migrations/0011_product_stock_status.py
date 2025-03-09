# Generated by Django 5.1.6 on 2025-03-09 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_category_image_alter_herosection_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_status',
            field=models.CharField(choices=[('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock')], default='in_stock', max_length=20),
        ),
    ]
