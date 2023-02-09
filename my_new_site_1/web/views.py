from timeit import default_timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def web_index(request: HttpRequest):
    products = [("Mango", 4), ("Dragon fruit", 6), ("Qiwi", 3)]
    context = {"products": products, }
    return render(request, 'web/index.html', context=context)


def about(request):
    people = [("Mark", 19), ("Alisa", 22), ("Stefan", None)]
    context = {"time": default_timer(), "people": people, }
    return render(request, 'web/about.html', context=context)
