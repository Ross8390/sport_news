from django.contrib import admin
from sport_news.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_date', 'update_date', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    readonly_fields = ['create_date', 'update_date']
    search_fields = ['title', 'content']
    list_filter = ['create_date', 'update_date', 'is_published']


admin.site.register(Article, ArticleAdmin)
