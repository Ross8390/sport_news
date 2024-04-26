from django.core.paginator import Paginator
from django.db.models import F
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from sport_news.forms import NewsForm
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

# def news_view(request):
#     # articles = Article.objects.order_by('-update_date')
#     page_number = int(request.GET.get("articles", 1))
#     # category = Category.objects.all()
#     paginator = Paginator(Article.objects.filter(is_published=True), 5)
#     articles = paginator.get_page(page_number)
#     return render(request, 'sport_news/news.html', {
#         'articles': articles,
#         'title': ''
#     })

class NewsView(ListView):
    model = Article
    template_name = 'sport_news/news.html'
    context_object_name = 'articles'
    paginate_by = 5
    # extra_context = {'title': 'Новости'}

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ''
        return context


# def category_view(request, category_id):
#     page_number = int(request.GET.get("articles", 1))
#     # category = Category.objects.all()
#     paginator = Paginator(Article.objects.filter(category_id=category_id, is_published=True), 5)
#     articles = paginator.get_page(page_number)
#     title_name = Category.objects.get(pk=category_id)
#     return render(request, 'sport_news/news.html', {
#         'articles': articles,
#         'title': title_name.title,
#         'category_id': category_id
#     })

class CategoryView(ListView):
    model = Article
    template_name = 'sport_news/news.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title_name = Category.objects.get(pk=self.kwargs['category_id'])
        context['title'] = title_name.title
        context['category_id'] = self.kwargs['category_id']
        return context


# def article_view(request, article_id):
#     # category = Category.objects.all()
#     # article = Article.objects.get(id=article_id, is_published=True)
#     article = get_object_or_404(Article, pk=article_id)
#     return render(request, 'sport_news/article.html', {
#         'title': article.title,
#         'article': article
#     })

class ArticleView(DetailView):
    model = Article
    template_name = 'sport_news/article.html'
    context_object_name = 'article'
    # slug_field = 'id'
    # slug_url_kwarg = 'article_id'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # obj = Article.objects.get(pk=self.kwargs['article_id'])
        # obj.views += 1
        # obj.save(update_fields=['views'])
        Article.objects.filter(pk=self.kwargs['article_id']).update(views=F('views') + 1)
        # title_name = Article.objects.get(pk=self.kwargs['article_id'])
        # context['title'] = title_name.title
        context['title'] = self.get_object().title
        return context



# def article_add(request):
#     if request.method == 'POST':
#         use_form = NewsForm(request.POST, request.FILES)
#         if use_form.is_valid():
#             obj = Article.objects.create(
#                 **use_form.cleaned_data
#                 )
#             obj.save()
#             return redirect(obj)
#     else:
#         use_form = NewsForm()
#     return render(request, 'sport_news/add_article.html', {'form': use_form})


# def article_add(request):
#     if request.method == 'POST':
#         use_form = NewsForm(request.POST, request.FILES)
#         if use_form.is_valid():
#             obj = use_form.save()
#             return redirect(obj)
#     else:
#         use_form = NewsForm()
#     return render(request, 'sport_news/add_article.html', {'form': use_form})

class ArticleAdd(CreateView):
    form_class = NewsForm
    template_name = 'sport_news/add_article.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context
