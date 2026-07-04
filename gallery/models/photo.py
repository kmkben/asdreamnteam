from django.db import models

from .album import Album


class Photo(models.Model):

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="photos",
    )

    image = models.ImageField(
        "Photo",
        upload_to="gallery/photos/",
    )

    title = models.CharField(
        "Titre",
        max_length=150,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "order",
            "-created_at",
        ]
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        if self.title:
            return self.title
        return f"Photo #{self.pk}"