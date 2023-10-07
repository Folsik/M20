from django.shortcuts import render
from django.views.generic import ListView
from .models import *
import logging

# Create your views here.

logger = logging.getLogger(__name__)

class ListArticlesView(ListView):
    template_name = "blogapp/articles-list.html"
    context_object_name = "articles"
    queryset = (
        Article.objects
        .defer("content")
        .select_related("author", "category")
        .prefetch_related("tags")
    )