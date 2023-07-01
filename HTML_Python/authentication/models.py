from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    # Deux profils possible "Utilisateur" ou "Administrateur"
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
                            default=UTILISATEUR)

    abonnement = models.ManyToManyField('self',
                                        symmetrical=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == "Utilisateur":
            group = Group.objects.get(name='Utilisateur')
            print(group)
            group.user_set.add(self)
        elif self.role == "Administrateur":
            group = Group.objects.get(name='Administrateur')
            group.user_set.add(self)

            """if self.role == "Utilisateur":
            group = Group.objects.get(name='Utilisateur')
            group.user_set.add(self)
        elif self.role == "Administrateur":
            group = Group.objects.get(name='Administrateur')
            group.user_set.add(self)"""