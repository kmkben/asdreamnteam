from django.db import models


class TrainingCategory(models.Model):

    name = models.CharField(
        "Nom",
        max_length=100,
        unique=True,
    )

    short_name = models.CharField(
        "Nom court",
        max_length=20,
        blank=True,
    )

    description = models.TextField(
        "Description",
        blank=True,
    )

    min_age = models.PositiveSmallIntegerField(
        "Âge minimum",
    )

    max_age = models.PositiveSmallIntegerField(
        "Âge maximum",
    )

    image = models.ImageField(
        "Image",
        upload_to="academy/categories/",
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        "Ordre",
        default=0,
    )

    is_active = models.BooleanField(
        "Active",
        default=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "order",
            "min_age",
        ]

        verbose_name = "Catégorie"

        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name