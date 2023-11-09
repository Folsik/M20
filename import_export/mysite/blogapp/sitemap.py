from django.contrib.sitemaps import Sitemap
from .models import Article


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Article.object.filter(published_at__isnull=False).orders_by("-published_at")

    def lastmod(self, obj: Article):
        return obj.published_at
