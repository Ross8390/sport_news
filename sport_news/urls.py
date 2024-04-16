from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from sport_news.views import article_add, NewsView, CategoryView, ArticleView

# urlpatterns = [
#     path('', news_view, name='main'),
#     path('category/<int:category_id>', category_view, name='cat'),
#     path('article/<int:article_id>', article_view, name='art'),
#     path('add_article/', article_add, name='add'),
# ]


urlpatterns = [
    path('', NewsView.as_view() , name='main'),
    path('category/<int:category_id>', CategoryView.as_view(), name='cat'),
    path('article/<int:article_id>', ArticleView.as_view(), name='art'),
    path('add_article/', article_add, name='add')
]