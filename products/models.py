from django.db import models
from django.utils.timezone import now


# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, help_text="Hex color code (e.g., #FF5733)")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name
        
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #image = models.ImageField(upload_to='products/', blank=True, null=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    colors = models.ManyToManyField(Color, blank=True)


    def __str__(self):
        return self.name
        
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"{self.product.name} Image"


class HeroSection(models.Model):
    title = models.CharField(max_length=100, default="New Collections")
    discount_text = models.CharField(max_length=50, default="20% OFF")
    button_text = models.CharField(max_length=20, default="Shop Now")
    button_link = models.URLField(default="#")
    image = models.ImageField(upload_to='hero_images/', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
        
class QRCode(models.Model):
    image = models.ImageField(upload_to='qr_codes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR Code {self.id}"


