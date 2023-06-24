from django.conf import settings
from django.db import models
from PIL import Image
from django import forms

# Classe pour les tickets
class Ticket(models.Model):
    titre = models.CharField(max_length=128)
    description = models.TextField(max_length=2048,
                                   blank=True)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               default="Demandeur inconnu",
                               on_delete=models.SET_DEFAULT)
    illustration = models.ImageField(default="../media/Pas_d'image_disponible.png")
    date_creation = models.DateTimeField(auto_now_add=True)
    nombre_critique = models.fields.IntegerField(default=0,
                                                 verbose_name="Nombre de critique")

    # Constance de classe pour plus de clarté
    ILLUSTRATIONS_TAILLE_MAX = (200, 200)

    # Methode de redimmensionnement
    def resize_illustration(self):
        # Ouverture de l'illustration
        illustration = Image.open(self.illustration)
        # Redimmensionnement de l'illustration
        illustration.thumbnail(self.ILLUSTRATIONS_TAILLE_MAX)
        # Sauvegarde en utilisant le chemin de l'illustration
        illustration.save(self.illustration.path)

    # Méthode super pour sauvegarder les illustrations
    def save(self,*arg, **kwargs):
        # Pour la compatibilité avec la classe parent
        super().save(*arg,**kwargs)
        # Appel de la méthode de redimmensionnement
        self.resize_illustration()
    
    def __str__(self):
        return f'{self.titre}'

# Classe pour les critiques
class Critique(models.Model):
    ticket = models.ForeignKey(Ticket,
                               on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(choices = ((0, '0'),
                                                       (1, '1'),
                                                       (2, '2'),
                                                       (3, '3'),
                                                       (4, '4'),
                                                       (5, '5')),
                                            default = 0)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    titre = models.CharField(max_length=128)
    commentaire = models.CharField(max_length=8192)
    date_creation = models.DateTimeField(auto_now_add=True)
