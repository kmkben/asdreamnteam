from django.db import models

from .category import TrainingCategory


class TrainingProgram(models.Model):

    category = models.ForeignKey(
        TrainingCategory,
        on_delete=models.CASCADE,
        related_name="programs",
    )

    title = models.CharField(
        "Titre",
        max_length=150,
    )

    description = models.TextField(
        "Description",
    )

    objectives = models.TextField(
        "Objectifs",
        blank=True,
    )

    image = models.ImageField(
        "Image",
        upload_to="academy/programs/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:

        ordering = [
            "order",
            "title",
        ]

        verbose_name = "Programme"

        verbose_name_plural = "Programmes"

    def __str__(self):
        return self.title