from django.contrib import admin
from .models import Category, HeroSection, Product, Color, ProductImage, QRCode
from orders.models import UPI

# Color Admin
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')  # Show ID, Name, and Image in list
    search_fields = ('name',)  # Enable search by name

# Hero Section Admin
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount_text', 'button_text')  # Display important fields
    list_editable = ('discount_text', 'button_text')  # Allow direct edits from list view
    search_fields = ('title',)  # Enable search

# Product Images Inline
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Allows adding multiple images at once

# Product Admin
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('id', 'name', 'category', 'price', 'old_price')  # Show important fields
    list_filter = ('category',)  # Add category filter
    search_fields = ('name', 'description')  # Enable search by name and description
    list_editable = ('price', 'old_price')  # Allow editing price directly
    filter_horizontal = ("colors",)  
    ordering = ('id',)  # Order products by ID

class UPIAdmin(admin.ModelAdmin):
    list_display = ('upi_id',)
    search_fields = ('upi_id',)

# Registering models with Django admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(QRCode)
admin.site.register(UPI)
