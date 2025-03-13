from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['product_list']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        try:
            return Product.objects.all()
        except Exception as e:
            import traceback
            print(f"Error in ProductSitemap.items(): {e}")
            print(traceback.format_exc())
            return []

    def location(self, obj):
        try:
         # Replace with your actual URL pattern name and required parameters
            return reverse('product_detail', kwargs={'pk': obj.pk})
        except Exception as e:
            print(f"Error in ProductSitemap.location(): {e}")
            return '/'

    def lastmod(self, obj):
        try:
            return obj.updated_at if hasattr(obj, 'updated_at') else None
        except Exception as e:
            print(f"Error in ProductSitemap.lastmod(): {e}")
            return None