from django import forms
from . import models

# Formulaire pour le ticket
class TicketForm(forms.ModelForm):
    # Permet la modification du ticket
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput,
                                     initial=True)
    class Meta :
        model = models.Ticket
        exclude = ("date_created","auteur")

class DeleteTicketForm(forms.Form):
    # Permet la suppression du ticket
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput,
                                     initial=True)


class ImageForm(forms.ModelForm):
    class Meta :
        model = models.Image
        fields = ["image"]