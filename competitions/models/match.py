from django.db import models

from .competition import Competition


class Match(models.Model):

    class Status(models.TextChoices):
        UPCOMING = "UPCOMING", "À venir"
        LIVE = "LIVE", "En cours"
        FINISHED = "FINISHED", "Terminé"
        POSTPONED = "POSTPONED", "Reporté"

    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name="matches",
        verbose_name="Compétition",
    )

    opponent = models.CharField(
        "Adversaire",
        max_length=150,
    )

    location = models.CharField(
        "Lieu",
        max_length=150,
    )

    match_date = models.DateTimeField(
        "Date",
    )

    home_match = models.BooleanField(
        "Match à domicile",
        default=True,
    )

    our_score = models.PositiveSmallIntegerField(
        "Score AS Dream Team",
        blank=True,
        null=True,
    )

    opponent_score = models.PositiveSmallIntegerField(
        "Score adverse",
        blank=True,
        null=True,
    )

    status = models.CharField(
        "Statut",
        max_length=20,
        choices=Status.choices,
        default=Status.UPCOMING,
    )

    note = models.TextField(
        "Commentaire",
        blank=True,
    )

    class Meta:
        ordering = ["-match_date"]
        verbose_name = "Match"
        verbose_name_plural = "Matchs"

    def __str__(self):
        return f"AS Dream Team vs {self.opponent}"