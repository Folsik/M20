from django.contrib.sitemaps import Sitemap
from .models import Product


class ShopSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Product.objects.filter(publishhed_at__isnull=False).order_bu("-product_details")

    def lastmod(self, obj: Product):
        return obj.product_details
