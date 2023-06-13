from django.conf import settings
from django.db import models
from PIL import Image

# Classe pour les illustrations
class Illustration(models.Model):
    illustration = models.ImageField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # Constance de classe pour plus de clarté
    ILLUSTRATIONS_MAX_SIZE = (800, 800)

    # Methode de redimmensionnement
    def resize_illustration(self):
        # Ouverture de l'illustration
        illustration = Image.open(self.illustration)
        # Redimmensionnement de l'illustration
        illustration.thumbnail(self.ILLUSTRATIONS_MAX_SIZE)
        # Sauvegarde en utilisant le chemin de l'illustration
        illustration.save(self.illustration.path)

    # Méthode super pour sauvegarder les illustrations
    def save(self,*arg, **kwargs):
        # Pour la compatibilité avec la classe parent
        super().save(*arg,**kwargs)
        # Appel de la méthode de redimmensionnement
        self.resize_illustration()

# Classe pour les critiques
class Critique(models.Model):
    illustration = models.ForeignKey(Illustration,
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     blank=True)
    titre = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               default="Auteur inconnu",
                               on_delete=models.SET_DEFAULT)
    date_created = models.DateTimeField(auto_now_add=True)

# Classe pour les tickets
class Ticket(models.Model):
    illustration = models.ForeignKey(Illustration,
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     blank=True)
    titre = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               default="Auteur inconnu",
                               on_delete=models.SET_DEFAULT)
    date_created = models.DateTimeField(auto_now_add=True)