from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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


class AbstractArticle(models.Model):
    objects = ArticleManager()
    name = models.TextField('название',
                            max_length=80,
                            help_text='Максимальная длина 80 символов')
    description = models.TextField('краткое описание',
                                   max_length=100,
                                   help_text='Максимальная длина 100 символов')
    is_published = models.BooleanField('опубликовано', default=True)
    text = models.TextField('статья', help_text='Содержание статьи')

    upload = models.ImageField('обложка',
                               upload_to='uploads/',
                               null=True)

    class Meta:
        abstract = True

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


class Article(AbstractArticle):
    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Breed(AbstractArticle):
    size = models.IntegerField('размер',
                               help_text='1 - маленький, 3 - большой',
                               validators=[MinValueValidator(1),
                                           MaxValueValidator(3)])
    activity = models.IntegerField('активность',
                                   help_text='1 - низкая, 3 - высокая',
                                   validators=[MinValueValidator(1),
                                               MaxValueValidator(3)])

    cost = models.IntegerField('стоимость содержания',
                               help_text='1 - низкая, 3 - высокая',
                               validators=[MinValueValidator(1),
                                           MaxValueValidator(3)])

    friendliness = models.IntegerField('дружелюбность',
                                       help_text='1 - низкая, 3 - высокая',
                                       validators=[MinValueValidator(1),
                                                   MaxValueValidator(3)])

    intellect = models.IntegerField('интеллект',
                                    help_text='1 - низкий, 3 - высокий',
                                    validators=[MinValueValidator(1),
                                                MaxValueValidator(3)])

    noise = models.IntegerField('шум',
                                help_text='1 - низкий, 3 - высокий',
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(3)])

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
