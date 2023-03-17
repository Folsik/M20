from django.contrib.auth.models import Group
from .models import Product, Order
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def shop_index(request: HttpRequest):
    products = {
        ("Laptop", 1999),
        ("Desktop", 2999),
        ("Smartphone", 999)
    }
    context = {
        "products": products
    }
    return render(request, 'shopapp/shop-app.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related("permissions").all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def order_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)
