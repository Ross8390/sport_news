from django.urls import path
from sport_news.views import news_view, category_view, article_view

urlpatterns = [
    path('', news_view, name='main'),
    path('category/<int:category_id>', category_view, name='cat'),
    path('article/<int:article_id>', article_view, name='art'),
]