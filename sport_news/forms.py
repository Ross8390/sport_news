from django import forms
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, Select, FileInput

from sport_news.models import Category, Article


# class NameModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return "%s" % obj.title
#

# class NewsForm(forms.Form):
#     title = forms.CharField(
#         label='Заголовок',
#         widget=forms.TextInput(attrs={'class': "form-control", 'style': 'width: 40rem'})
#         )
#     content = forms.CharField(
#         label='Статья',
#         widget=forms.Textarea(attrs={'class': "form-control", 'style': 'width: 40rem'})
#         )
#     is_published = forms.BooleanField(
#         label='Опубликовать',
#         required=False,
#         widget=forms.CheckboxInput(attrs={'class': "form-check-input"})
#         )
#     category = NameModelChoiceField(
#         label='Категория',
#         queryset=Category.objects.order_by('id'),
#         widget=forms.Select(attrs={'select class': "form-select", 'style': 'width: 15rem'})
#         )
#     image = forms.ImageField(
#         required=False,
#         widget=forms.FileInput(attrs={'select class': "form-select", 'style': 'width: 40rem'})
#         )

class NewsForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'is_published', 'category', 'image']
        widgets = {
            'title': TextInput(attrs={'class': "form-control", 'style': 'width: 40rem'}),
            'content': Textarea(attrs={'class': "form-control", 'style': 'width: 40rem'}),
            'is_published': CheckboxInput(attrs={'class': "form-check-input"}),
            'category': Select(attrs={'select class': "form-select", 'style': 'width: 15rem'}),
            'image': FileInput(attrs={'select class': "form-select", 'style': 'width: 40rem'})
        }


class FeedbackForm(forms.Form):
    title = forms.CharField(
        label='Тема',
        widget=forms.TextInput(attrs={'class': "form-control", 'style': 'width: 40rem'})
    )
    content = forms.CharField(
        label='Текст',
        widget=forms.Textarea(attrs={'class': "form-control", 'style': 'width: 40rem'})
    )
