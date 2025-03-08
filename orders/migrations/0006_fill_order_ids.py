from django.db import migrations
import random
import string

def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def fill_order_ids(apps, schema_editor):
    Order = apps.get_model('orders', 'Order')
    
    for order in Order.objects.filter(order_id__isnull=True):
        while True:
            new_order_id = generate_order_id()
            if not Order.objects.filter(order_id=new_order_id).exists():
                order.order_id = new_order_id
                order.save()
                break

class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0005_order_order_id'),  # Ensure the name matches exactly!
    ]

    operations = [
        migrations.RunPython(fill_order_ids),
    ]