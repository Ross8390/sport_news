from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from sport_news.views import NewsView, CategoryView, ArticleView, ArticleAdd, user_register, user_login, user_logout, \
    feedback_add

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
    path('add_article/', ArticleAdd.as_view(), name='add'),
    path('user_register/', user_register, name='register'),
    path('user_login/', user_login, name='login'),
    path('user_logout/', user_logout, name='logout'),
    path('feedback_add/', feedback_add, name='feedback')
]