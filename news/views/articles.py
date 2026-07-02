from django.shortcuts import render

from news.models import NewsArticle


def articles(request):

    return render(
        request,
        "news/articles.html",
        {
            "page": "news",
            "articles": NewsArticle.objects.filter(
                is_published=True,
            ),
        },
    )