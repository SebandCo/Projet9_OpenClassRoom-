from django import forms
from django.contrib.auth import get_user_model
# Récupération du modèle prédéfini UserCreationForm
from django.contrib.auth.forms import UserCreationForm

class ModificationUtilisateur(forms.ModelForm):
    edit_user = forms.BooleanField(widget=forms.HiddenInput,
                                   initial=True)
    class Meta:
        # Import du modèle User 
        model = get_user_model()
        fields = ["role"]
