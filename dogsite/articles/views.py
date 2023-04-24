from django.shortcuts import get_object_or_404, render

from articles.models import Article


def article_list(request):
    template_name = 'articles/index.html'

    if request.path == '/articles/':
        is_breeds = False
        articles = Article.objects.published().filter(is_breed=False)
    else:
        is_breeds = True
        articles = Article.objects.published().filter(is_breed=True)

    context = {
        'articles': articles,
        'is_breeds': is_breeds,
    }
    return render(request, template_name, context)


def article(request, pk):
    template_name = 'articles/detail.html'

    article = get_object_or_404(
        Article.objects.published_one(pk))

    context = {
        'article': article,
    }
    return render(request, template_name, context)
