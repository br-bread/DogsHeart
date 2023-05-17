from django.shortcuts import get_object_or_404, render
from re import compile

from .models import Article, Breed
from . import forms


def article_list(request):
    template_name = 'articles/index.html'

    if request.path == '/articles/':
        articles = Article.objects.published()
        context = {
            'articles': articles,
        }
    else:
        form = forms.BreedForm(request.GET or None)
        articles = Breed.objects.published()
        if form.is_valid():

            kwargs = {k: v for k, v in form.cleaned_data.items() if v}
            articles = Breed.objects.published().filter(**kwargs)

        context = {
            'articles': articles,
            'form': form,
        }

    return render(request, template_name, context)


def article(request, pk):
    template_name = 'articles/detail.html'

    if compile('/articles/(?P<pk>[1-9]\\d*)/$').match(request.path):
        article = get_object_or_404(
            Article.objects.published_one(pk))
    else:
        article = get_object_or_404(
            Breed.objects.published_one(pk))

    context = {
        'article': article,
    }
    return render(request, template_name, context)
