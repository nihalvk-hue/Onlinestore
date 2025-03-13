from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product  # Ensure this is correct

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['product_list']  # Make sure this matches your URL names

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        try:
            products = Product.objects.all()
            return products
        except Exception as e:
            print(f"Error fetching products: {e}")  # Debugging
            return []

    def lastmod(self, obj):
        return obj.created_at_at if hasattr(obj, 'created_at') else None