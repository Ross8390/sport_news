from django.urls import path
from sport_news.views import news_view

urlpatterns = [
    path('news/', news_view),
]