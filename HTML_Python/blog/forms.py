from django import forms
from django.contrib.auth import get_user_model
from . import models
from django import forms

# Formulaire pour le ticket
class TicketForm(forms.ModelForm):
    # Permet la modification du ticket
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput,
                                     initial=True)
    class Meta :
        model = models.Ticket
        exclude = ("date_creation","auteur","nombre_critique")

# Formulaire pour la partie critique
# Formulaire pour la critique
class CritiqueForm(forms.ModelForm):
    # Permet la modification du ticket
    edit_critique = forms.BooleanField(widget=forms.HiddenInput,
                                   initial=True)
    class Meta :
        model = models.Critique
        exclude = ("date_creation","auteur")
        widgets = {'note': forms.RadioSelect()}
