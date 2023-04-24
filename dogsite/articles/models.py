from django.db import models


class ArticleManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .order_by('name')
                .only('name', 'description',)
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

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.name
