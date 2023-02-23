from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write("No order found")
            return
        prducts = Product.objects.all()
        for product in prducts:
            order.products.add(product)

        order.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully adds products {order.products.all()} to order {order}"))
