from django.shortcuts import render
from .models import Product, Other

# Create your views here.


def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'Hello', 'name'],
        "products": Product.objects.all()
    }
    return render(request, 'mainsite/main.html',  data)


def about(request):
    data = {
        "other": Other.objects.select_related("user").prefetch_related("products").all()
    }
    return render(request, 'mainsite/about.html', data)


def contact(request):
    return render(request, 'mainsite/contact.html')


