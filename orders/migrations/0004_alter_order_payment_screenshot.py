# Generated by Django 5.1.6 on 2025-03-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_payment_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_screenshot',
            field=models.FileField(blank=True, null=True, upload_to='payment_screenshots/'),
        ),
    ]
