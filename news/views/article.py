from django.shortcuts import get_object_or_404
from django.shortcuts import render

from news.models import NewsArticle


def article(request, slug):

    return render(
        request,
        "news/article.html",
        {
            "page": "news",
            "article": get_object_or_404(
                NewsArticle,
                slug=slug,
                is_published=True,
            ),
        },
    )