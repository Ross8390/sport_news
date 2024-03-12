from django.contrib import admin
from sport_news.models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'create_date', 'update_date', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    readonly_fields = ['create_date', 'update_date']
    search_fields = ['title', 'content']
    list_filter = ['create_date', 'category', 'update_date', 'is_published']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

