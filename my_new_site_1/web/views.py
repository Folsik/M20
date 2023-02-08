from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def web_index(request: HttpRequest):
    print(request.path)
    print(request.method)
    print(request.headers)
    return render(request, 'web/index.html')


def about(request):
    return render(request, 'web/about.html')
