from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Deux profils d'utilisateur possible Utilisateur ou Administrateur
    UTILISATEUR = "UTILISATEUR"
    ADMINISTRATEUR = "ADMINISTRATEUR"

    ROLE_CHOICES = (
        {UTILISATEUR, "Utilisateur"},
        {ADMINISTRATEUR, "Administrateur"}
    )

    nombre_ticket = models.fields.IntegerField(default=0,
                                               verbose_name="Nombre de ticket")
    nombre_critique = models.fields.IntegerField(default=0,
                                                 verbose_name="Nombre de critique")
    role = models.CharField(max_length=30,
                            choices=ROLE_CHOICES,
                            verbose_name="Rôle")
