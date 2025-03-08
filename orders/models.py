import random
import string
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product, Color
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

def generate_order_id():
    """Generate a unique 5-character alphanumeric order ID."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    order_id = models.CharField(max_length=5, unique=True, editable=False, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    alt_phone = models.CharField(max_length=15, blank=True, null=True)  # Alternative mobile number
    email = models.EmailField()
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_screenshot = CloudinaryField('payment_screenshots', blank=True, null=True)  # Use CloudinaryField
    upi_transaction_id = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    selected_color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    payment_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.order_id} - {self.name} ({self.product.name if self.product else 'No Product'})"

    def save(self, *args, **kwargs):
        """Ensure unique order_id and set total_price."""
        if not self.order_id:
            while True:
                new_order_id = generate_order_id()
                if not Order.objects.filter(order_id=new_order_id).exists():
                    self.order_id = new_order_id
                    break

        if not self.total_price:
            try:
                self.total_price = self.product.price if self.product else 0
            except ObjectDoesNotExist:
                self.total_price = 0

        super().save(*args, **kwargs)
        
class UPI(models.Model):
    upi_id = models.CharField(max_length=100, unique=True, help_text="Enter the UPI ID for payments")

    def __str__(self):
        return self.upi_id