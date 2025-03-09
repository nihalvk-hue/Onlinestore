from django.db import models
from django.utils.timezone import now
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, help_text="Hex color code (e.g., #FF5733)")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = CloudinaryField('category_images', blank=True, null=True)  # Use CloudinaryField instead of ImageField

    def __str__(self):
        return self.name

class Product(models.Model):
    STOCK_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    colors = models.ManyToManyField(Color, blank=True)
    stock_status = models.CharField(
        max_length=20, choices=STOCK_CHOICES, default='in_stock'
    )

    def is_available(self):
        return self.stock_status == 'in_stock'

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = CloudinaryField('product_images')  # Use CloudinaryField

    def __str__(self):
        return f"{self.product.name} Image"

class HeroSection(models.Model):
    title = models.CharField(max_length=100, default="New Collections")
    discount_text = models.CharField(max_length=50, default="20% OFF")
    button_text = models.CharField(max_length=20, default="Shop Now")
    button_link = models.URLField(default="#")
    image = CloudinaryField('hero_images', blank=True, null=True)  # Use CloudinaryField
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class QRCode(models.Model):
    image = CloudinaryField('qr_codes')  # Use CloudinaryField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR Code {self.id}"