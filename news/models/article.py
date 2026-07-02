from django.db import models
from django.urls import reverse


class NewsArticle(models.Model):

    title = models.CharField(
        "Titre",
        max_length=200,
    )

    slug = models.SlugField(
        unique=True,
    )

    summary = models.TextField(
        "Résumé",
    )

    content = models.TextField(
        "Contenu",
    )

    image = models.ImageField(
        "Image",
        upload_to="news/articles/",
        blank=True,
        null=True,
    )

    published_at = models.DateTimeField(
        "Date de publication",
        auto_now_add=True,
    )

    is_published = models.BooleanField(
        "Publié",
        default=True,
    )

    featured = models.BooleanField(
        "Article à la une",
        default=False,
    )

    class Meta:

        ordering = [
            "-featured",
            "-published_at",
        ]

        verbose_name = "Article"

        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "news:article",
            kwargs={
                "slug": self.slug,
            },
        )