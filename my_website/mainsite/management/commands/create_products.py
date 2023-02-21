from django.core.management import BaseCommand
from mainsite.models import Product


class Command(BaseCommand):
    """This is command create new product"""
    def handle(self, *args, **options):
        self.stdout.write("Create product")
        products_names = ["fruit", "vegetables", "juice"]
        for products_name in products_names:
            products, created = Product.objects.get_or_create(name=products_name)
            self.stdout.write(f"Create product {products.name}")
        self.stdout.write(self.style.SUCCESS("Product Create"))