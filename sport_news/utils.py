from django.views.generic import ListView

from sport_news.models import Article


class NewsQuerysetMixin(ListView):
    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')