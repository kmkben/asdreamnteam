from django.db import models


class Competition(models.Model):

    name = models.CharField(
        "Nom",
        max_length=150,
    )

    description = models.TextField(
        "Description",
        blank=True,
    )

    season = models.CharField(
        "Saison",
        max_length=20,
        blank=True,
    )

    logo = models.ImageField(
        "Logo",
        upload_to="competitions/logos/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        "Active",
        default=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Compétition"
        verbose_name_plural = "Compétitions"

    def __str__(self):
        return self.name