from django.shortcuts import render
from .models import Artiles
from .forms import ArtilesForm
# Create your views here.


def news(request):
    news_today = Artiles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news_today': news_today})


def create(request):
    form = ArtilesForm()

    data = {
        'form': form
    }
    return render(request, 'news/create.html')
