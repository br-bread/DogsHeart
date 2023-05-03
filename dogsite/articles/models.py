from django.db import models

from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class ArticleManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .order_by('name')
                .only('name', 'description')
        )

    def published_one(self, pk):
        return (
            self.get_queryset()
                .filter(is_published=True, pk=pk)
                .only('name', 'description', 'text')
        )


class Article(models.Model):
    objects = ArticleManager()
    name = models.TextField('название',
                            max_length=40,
                            help_text='Максимальная длина 40 символов')
    is_breed = models.BooleanField('статья о породе', default=False)
    description = models.TextField('краткое описание',
                                   max_length=100,
                                   help_text='Максимальная длина 100 символов')
    is_published = models.BooleanField('опубликовано', default=True)
    text = models.TextField('статья', help_text='Содержание статьи')

    upload = models.ImageField('обложка',
                               upload_to='uploads/',
                               null=True)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.name

    @property
    def get_img_tmb(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '650x400', crop='center', quality=80)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img_tmb.url}" '
                f'class="rounded float-start">'
            )
        return "Нет изображения"

    def image(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return "Нет изображения"

    image_tmb.short_description = 'обложка'
    image_tmb.allow_tags = True
