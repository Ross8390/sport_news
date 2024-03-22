from django.http import HttpResponse
from django.shortcuts import render

from sport_news.models import Article, Category


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
    articles = Article.objects.filter(is_published=True)
    category = Category.objects.all()
    return render(request, 'sport_news/news.html', {
        'articles': articles,
        'title': 'Новости',
        'category': category
    })


def category_view(request, category_id):
    articles = Article.objects.filter(category_id=category_id, is_published=True)
    category = Category.objects.all()
    title_name = Category.objects.get(pk=category_id)
    return render(request, 'sport_news/news.html', {
        'articles': articles,
        'title': title_name.title,
        'category': category
    })


def article_view(request, article_id):
    articles = Article.objects.filter(id=article_id, is_published=True)
    category = Category.objects.all()
    title_name = Article.objects.get(id=article_id)
    return render(request, 'sport_news/article.html', {
        'articles': articles,
        'title': title_name.title,
        'category': category
    })