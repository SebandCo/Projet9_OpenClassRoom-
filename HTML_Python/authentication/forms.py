from django import forms
from django.contrib.auth import get_user_model
# Récupération du modèle prédéfini UserCreationForm
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    edit_user = forms.BooleanField(widget=forms.HiddenInput,
                                   initial=True)

    class Meta(UserCreationForm.Meta):
        # Import du modèle User
        model = get_user_model()
        # Rajout de champs en plus du mot de passe
        fields = ["username",
                  "email",
                  "first_name",
                  "last_name"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,
                               label="Nom d'utilisateur")
    password = forms.CharField(max_length=63,
                               widget=forms.PasswordInput,
                               label="Mot de passe")
