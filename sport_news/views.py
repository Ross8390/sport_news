from django.core.paginator import Paginator
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
    page_number = int(request.GET.get("articles", 1))
    category = Category.objects.all()
    paginator = Paginator(Article.objects.filter(is_published=True), 5)
    articles = paginator.get_page(page_number)
    return render(request, 'sport_news/news.html', {
        'articles': articles,
        'title': '',
        'category': category
    })


def category_view(request, category_id):
    page_number = int(request.GET.get("articles", 1))
    category = Category.objects.all()
    paginator = Paginator(Article.objects.filter(category_id=category_id, is_published=True), 5)
    articles = paginator.get_page(page_number)
    title_name = Category.objects.get(pk=category_id)
    return render(request, 'sport_news/news.html', {
        'articles': articles,
        'title': title_name.title,
        'category': category,
        'category_id': category_id
    })


def article_view(request, article_id):
    category = Category.objects.all()
    article = Article.objects.get(id=article_id, is_published=True)
    return render(request, 'sport_news/article.html', {
        'title': article.title,
        'article': article,
        'category': category
    })
