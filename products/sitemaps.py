from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product  # Import your Product model

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['product_list', 'product_detail', 'contact_view']  # Use your actual view names

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.all()

   # def lastmod(self, obj):
  #\      return obj.created_at  # If you have 'updated_at', use that