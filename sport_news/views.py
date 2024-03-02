from django.http import HttpResponse
from django.shortcuts import render

from sport_news.models import Article


def news_view(request):
    articles = Article.objects.all()
    str1 = f'<title>Новости</title>'
    for news in reversed(articles):
        str1 += f'<body>' \
                f'<h3>{news.title}</h3>' \
                f'<p>{news.content}</p>' \
                f'<p>{news.create_date.strftime("%Y-%m-%d %H:%M:%S")}</p>' \
                f'</body>'
    print(str1)
    return HttpResponse(str1)
