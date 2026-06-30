from django.db import models


class Partner(models.Model):
    name = models.CharField("Nom", max_length=150)
    logo = models.ImageField("Logo", upload_to="team/partners/", blank=True, null=True)
    website = models.URLField("Site web", blank=True)
    description = models.TextField("Description", blank=True)

    is_active = models.BooleanField("Actif", default=True)
    order = models.PositiveIntegerField("Ordre d’affichage", default=0)

    created_at = models.DateTimeField("Créé le", auto_now_add=True)
    updated_at = models.DateTimeField("Modifié le", auto_now=True)

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name