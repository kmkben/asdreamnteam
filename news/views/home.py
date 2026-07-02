from django.shortcuts import render

from news.models import NewsArticle


def home(request):

    featured = NewsArticle.objects.filter(
        featured=True,
        is_published=True,
    )[:1]

    articles = NewsArticle.objects.filter(
        is_published=True,
    )[:6]

    return render(
        request,
        "news/home.html",
        {
            "page": "news",
            "featured": featured.first(),
            "articles": articles,
        },
    )