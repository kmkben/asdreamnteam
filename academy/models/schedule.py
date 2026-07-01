from django.db import models

from .category import TrainingCategory


class TrainingSchedule(models.Model):
    class WeekDay(models.TextChoices):
        MONDAY = "MONDAY", "Lundi"
        TUESDAY = "TUESDAY", "Mardi"
        WEDNESDAY = "WEDNESDAY", "Mercredi"
        THURSDAY = "THURSDAY", "Jeudi"
        FRIDAY = "FRIDAY", "Vendredi"
        SATURDAY = "SATURDAY", "Samedi"
        SUNDAY = "SUNDAY", "Dimanche"

    category = models.ForeignKey(
        TrainingCategory,
        on_delete=models.CASCADE,
        related_name="schedules",
        verbose_name="Catégorie",
    )

    day = models.CharField(
        "Jour",
        max_length=20,
        choices=WeekDay.choices,
    )

    start_time = models.TimeField("Heure de début")
    end_time = models.TimeField("Heure de fin")

    location = models.CharField(
        "Lieu",
        max_length=150,
        blank=True,
    )

    note = models.CharField(
        "Note",
        max_length=255,
        blank=True,
    )

    is_active = models.BooleanField("Actif", default=True)

    class Meta:
        verbose_name = "Horaire d'entraînement"
        verbose_name_plural = "Horaires d'entraînement"
        ordering = ["category", "day", "start_time"]

    def __str__(self):
        return f"{self.category} - {self.get_day_display()} {self.start_time:%H:%M}"