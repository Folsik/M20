from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'Hello', 'name']
    }
    return render(request, 'mainsite/main.html', data)


def about(request):
    return render(request, 'mainsite/about.html')


def contact(request):
    return render(request, 'mainsite/contact.html')