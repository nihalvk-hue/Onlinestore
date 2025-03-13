from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product  # Assuming you have a Product model

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['product_list', 'homepage']  # Add your important views

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.created_at  # Make sure your Product model has an "updated_at" field 