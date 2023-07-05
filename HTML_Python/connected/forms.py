from django import forms
# Récupération du modèle prédéfini UserCreationForm
from authentication.models import User


class ModificationUtilisateur(forms.ModelForm):
    edit_user = forms.BooleanField(widget=forms.HiddenInput,
                                   initial=True)

    class Meta:
        # Import du modèle User
        model = User
        fields = ["role"]


class FollowerForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["abonnement"]
