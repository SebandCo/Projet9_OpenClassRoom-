from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.shortcuts import get_object_or_404


# ------------- Gestion des critiques ----------------
@login_required
def creation_critique_vide(request):
    critique_form = forms.CritiqueForm()
    if request.method == "POST":
        critique_form = forms.CritiqueForm(request.POST)
        # On vérifie que le formulaire est valide
        if critique_form.is_valid():
            critique = critique_form.save(commit=False)
            critique.auteur = request.user
            critique.save()
            # Augmente de 1 le nombre de critique cumulé pour le titre
            critique.ticket.nombre_critique += 1
            critique.ticket.save()
            # Augmente de 1 le nombre de critique posté par l'utilisateur
            request.user.nombre_critique += 1
            request.user.save()
            return redirect("home")

    return render(request,
                  "blog/creation_critique_vide.html",
                  context={"critique_form": critique_form})


@login_required
def creation_critique_liee(request, ticket_id):
    critique_form = forms.CritiqueLieeForm()
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == "POST":
        critique_form = forms.CritiqueLieeForm(request.POST)
        # On vérifie que le formulaire est valide
        if critique_form.is_valid():
            critique = critique_form.save(commit=False)
            critique.auteur = request.user
            critique.ticket = ticket
            critique.save()
            # Augmente de 1 le nombre de critique cumulé pour le titre
            critique.ticket.nombre_critique += 1
            critique.ticket.save()
            # Augmente de 1 le nombre de critique posté par l'utilisateur
            request.user.nombre_critique += 1
            request.user.save()
            return redirect("home")

    return render(request,
                  "blog/creation_critique_liee.html",
                  context={"critique_form": critique_form,
                           "ticket": ticket})


@login_required
def modification_critique(request, critique_id):
    critique = get_object_or_404(models.Critique, id=critique_id)
    critique_form = forms.CritiqueLieeForm(instance=critique)
    if request.method == "POST":
        if "edit_critique" in request.POST:
            # Controle que la personne qui modifie est bien le createur de la critique
            if request.user == critique.auteur:
                critique_form = forms.CritiqueLieeForm(request.POST,
                                                       request.FILES,
                                                       instance=critique)
                # On vérifie que le formulaire est valide
                if critique_form.is_valid():
                    critique_form.save()
            return redirect("home")

    return render(request,
                  "blog/modification_critique.html",
                  context={"critique_form": critique_form,
                           "ticket": critique.ticket})


@login_required
def suppression_critique(request, critique_id):
    critique = models.Critique.objects.get(id=critique_id)
    if request.method == "POST":
        # Controle que la personne qui supprime est bien le createur de la critique
        if request.user == critique.auteur:
            # Diminue de 1 le nombre de critique du ticket
            critique.ticket.nombre_critique -= 1
            critique.ticket.save()
            # Diminue de 1 le nombre de critique posté par l'utilisateur
            request.user.nombre_critique -= 1
            request.user.save()
            # Supprime la critique
            critique.delete()
        return redirect("home")

    return render(request,
                  "blog/suppression_critique.html",
                  context={"critique": critique})


# ------------- Gestion des tickets ----------------
@login_required
def creation_ticket(request):
    print(dir(request.user))
    ticket_form = forms.TicketForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST,
                                       request.FILES)
        # On vérifie que le formulaire est valide
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.auteur = request.user
            ticket.save()
            # Augmente de 1 le nombre de critique posté par l'utilisateur
            request.user.nombre_ticket += 1
            request.user.save()
            return redirect("home")

    return render(request,
                  "blog/creation_ticket.html",
                  context={"ticket_form": ticket_form})


@login_required
def modification_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    ticket_form = forms.TicketForm(instance=ticket)
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            # Controle que la personne qui modifie est bien le createur du ticket
            if request.user == ticket.auteur:
                ticket_form = forms.TicketForm(request.POST,
                                               request.FILES,
                                               instance=ticket)
                # On vérifie que le formulaire est valide
                if ticket_form.is_valid():
                    ticket_form.save()
            return redirect("home")

    return render(request,
                  "blog/modification_ticket.html",
                  context={"ticket_form": ticket_form})


@login_required
def affichage_des_tickets(request):
    tickets = models.Ticket.objects.all()
    return render(request,
                  "blog/affichage_des_tickets.html",
                  context={"tickets": tickets})


@login_required
def affichage_dun_ticket(request, ticket_id):
    ticket_choisi = get_object_or_404(models.Ticket, id=ticket_id)
    critiques = models.Critique.objects.filter(ticket=ticket_choisi)
    # Vérifie que l'utilisateur n'a pas déjà mis une critique
    critique_existante = False
    for critique in critiques:
        if critique.auteur == request.user:
            critique_existante = True

    return render(request,
                  "blog/affichage_dun_ticket.html",
                  context={"ticket": ticket_choisi,
                           "critiques": critiques,
                           "critique_existante": critique_existante})


@login_required
def suppression_ticket(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        # Controle que la personne qui supprime est bien le createur du ticket
        if request.user == ticket.auteur:
            # Diminue de 1 le nombre de ticket posté par l'utilisateur
            request.user.nombre_ticket -= 1
            request.user.save()
            # Supprime le ticket
            ticket.delete()
        return redirect("home")

    return render(request,
                  "blog/suppression_ticket.html",
                  context={"ticket": ticket})
