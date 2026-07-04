from django.db import models
from django.urls import reverse


class Album(models.Model):

    title = models.CharField(
        "Titre",
        max_length=150,
    )

    slug = models.SlugField(
        unique=True,
    )

    description = models.TextField(
        "Description",
        blank=True,
    )

    cover = models.ImageField(
        "Image de couverture",
        upload_to="gallery/albums/",
        blank=True,
        null=True,
    )

    is_published = models.BooleanField(
        "Publié",
        default=True,
    )

    featured = models.BooleanField(
        "À la une",
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "-featured",
            "-created_at",
        ]
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "gallery:album",
            kwargs={"slug": self.slug},
        )