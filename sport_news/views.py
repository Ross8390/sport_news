from django.http import HttpResponse
from django.shortcuts import render

from sport_news.models import Article


# def news_view(request):
#     articles = Article.objects.order_by('-update_date')
#     str1 = f'<title>Новости</title>'
#     for news in articles:
#         str1 += f'<body>' \
#                 f'<h3>{news.title}</h3>' \
#                 f'<p>{news.content}</p>' \
#                 f'<p>{news.create_date.strftime("%Y-%m-%d %H:%M:%S")}</p>' \
#                 f'</body>'
#     print(str1)
#     return HttpResponse(str1)

def news_view(request):
     # articles = Article.objects.order_by('-update_date')
     articles = Article.objects.all()
     return render(request, 'sport_news/news.html', {'articles': articles, 'title': 'Новости'})