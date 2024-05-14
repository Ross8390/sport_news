import datetime
from django import template
from django.core.cache import cache

from sport_news.models import Category

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def category_tag():
    return Category.objects.all()


@register.inclusion_tag('sport_news/categories.html')
def category_inc(category_id):
    category = cache.get('category')
    if not category:
        category = Category.objects.all()
        cache.set('category', category, 60)
    return {
        'category': category,
        'category_id': category_id
    }