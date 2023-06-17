from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from . import forms, models


@login_required
def creation_critique(request):
    critique_form = forms.CritiqueForm()
    #print(utilisateur)
    if request.method == "POST":
        #critique_titre = forms.CritiqueTitre(request.POST)
        critique_form = forms.CritiqueForm(request.POST)
        # On vérifie que le formulaire est valide
        if critique_form.is_valid():
            critique = critique_form.save(commit=False) 
            critique.auteur = request.user
            critique.save()
            # Augmente de 1 le nombre de critique posté par l'utilisateur
            request.user.nombre_critique += 1
            request.user.save()
            return redirect("home")
    context = {"critique_form": critique_form}
    return render(request,
                  "blog/creation_critique.html",
                  context = context)


@login_required
def creation_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == "POST":
        ticket_form= forms.TicketForm(request.POST, request.FILES)
        # On vérifie que le formulaire est valide
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.auteur = request.user
            ticket.save()
            # Augmente de 1 le nombre de ticket posté par l'utilisateur
            request.user.nombre_ticket += 1
            request.user.save()
            return redirect("home")
    context ={"ticket_form": ticket_form}
    return render(request,
                  "blog/creation_ticket.html",
                  context = context)