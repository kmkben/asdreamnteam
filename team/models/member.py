from django.db import models


class ClubMember(models.Model):
    class Role(models.TextChoices):
        PRESIDENT = "PRESIDENT", "Président"
        VICE_PRESIDENT = "VICE_PRESIDENT", "Vice-président"
        COACH = "COACH", "Coach"
        ASSISTANT_COACH = "ASSISTANT_COACH", "Coach adjoint"
        PLAYER = "PLAYER", "Joueur"
        STAFF = "STAFF", "Staff"
        MANAGER = "MANAGER", "Manager"
        OTHER = "OTHER", "Autre"

    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)
    role = models.CharField("Rôle", max_length=30, choices=Role.choices)

    position = models.CharField("Poste", max_length=100, blank=True)
    category = models.CharField("Catégorie", max_length=50, blank=True)

    photo = models.ImageField("Photo", upload_to="team/members/", blank=True, null=True)

    bio = models.TextField("Biographie", blank=True)

    is_active = models.BooleanField("Actif", default=True)
    order = models.PositiveIntegerField("Ordre d’affichage", default=0)

    created_at = models.DateTimeField("Créé le", auto_now_add=True)
    updated_at = models.DateTimeField("Modifié le", auto_now=True)

    class Meta:
        verbose_name = "Membre du club"
        verbose_name_plural = "Membres du club"
        ordering = ["order", "last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"