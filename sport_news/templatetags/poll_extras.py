import datetime
from django import template

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
    category = Category.objects.all()
    return {
        'category': category,
        'category_id': category_id
    }