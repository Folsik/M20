from django.contrib.auth.models import User
from django.core.management import BaseCommand
from mainsite.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="Moscow",
            promocode="LOL",
            user=user,
        )
        self.stdout.write(f"Create order {order}")