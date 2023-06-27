from django import forms
from django.contrib.auth import get_user_model
# Récupération du modèle prédéfini UserCreationForm
from authentication.models import User

class ModificationUtilisateur(forms.ModelForm):
    edit_user = forms.BooleanField(widget=forms.HiddenInput,
                                   initial=True)
    
    class Meta:
        # Import du modèle User 
        model = User
        fields = ["role"]

Users = get_user_model()

class FollowerForm(forms.ModelForm):
    
    class Meta :
        model = User
        fields = ["abonnement"]
