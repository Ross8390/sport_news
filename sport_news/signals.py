from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from sport_news.models import Article


@receiver(post_save, sender=Article)
def article_created(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'new article',
            f'Новая статья "{instance.title}" добавлена',
            settings.EMAIL_HOST_USER,
            ['bogomolovog@mail.ru'],
        )
