from django.contrib.syndication.views import Feed
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
from .models import Article
# Create your views here.


class ArticleListView(ListView):
    queryset =(
        Article.objects
        .filter(published_at__isnull=False)
        .orders_by("-published_at")
    )


class ArticleDetailView(DetailView):
    model = Article


class LatestArticlesFeed(Feed):
    title = "blog articles (latest)"
    description = "updates on changes and addition blog articles"
    link = reverse_lazy("blogapp:articles")

    def items(self):
        return (
            Article.objects
            .filter(published_at__isnull=False)
            .orders_by("-published_at")[:5]
        )

    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return item.body[:200]
