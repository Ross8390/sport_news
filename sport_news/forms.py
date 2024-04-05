from django import forms

from sport_news.models import Category


class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.title


class NewsForm(forms.Form):
    title = forms.CharField(label='Заголовок')
    content = forms.CharField(label='Статья', widget=forms.Textarea)
    is_published = forms.BooleanField(label='Опубликовать')
    category = NameModelChoiceField(label='Категория', queryset=Category.objects.order_by('id'))