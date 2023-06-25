from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.shortcuts import get_object_or_404

# ------------- Gestion des critiques ----------------
def creation_critique(request):
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
                  "blog/creation_critique.html",
                  context = {"critique_form": critique_form})

def modification_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    ticket_form = forms.TicketForm(instance=ticket)
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            ticket_form = forms.TicketForm(request.POST,
                                           request.FILES,
                                           instance=ticket)
            # On vérifie que le formulaire est valide
            if ticket_form.is_valid():
                ticket_form.save()
                return redirect("home")
    return render(request,
                  "blog/modification_ticket.html",
                  context = {"ticket_form": ticket_form})

# ------------- Gestion des tickets ----------------
def creation_ticket(request):
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
                  context = {"ticket_form": ticket_form})


'''@login_required
def creation_ticket(request):
    ticket_form = forms.TicketForm()
    critique_form = forms.TicketEtCritiqueForm()
    if request.method == "POST":
        ticket_form= forms.TicketForm(request.POST, request.FILES)
        critique_form= forms.TicketEtCritiqueForm(request.POST)
        # On vérifie que le formulaire est valide
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.auteur = request.user
            ticket.save()
            # Augmente de 1 le nombre de ticket posté par l'utilisateur
            request.user.nombre_ticket += 1
            request.user.save()
            print(critique_form)
            if critique_form.is_valid():
                critique = critique_form.save(commit=False) 
                critique.auteur = request.user
                print(ticket.id)
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
                  "blog/creation_ticket.html",
                  context = {"ticket_form": ticket_form,
                             "critique_form": critique_form})'''

@login_required
def affichage_des_tickets(request):
    tickets = models.Ticket.objects.all()
    return render(request,
                  "blog/affichage_des_tickets.html",
                  context={"tickets":tickets})

@login_required
def affichage_dun_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request,
                  "blog/affichage_dun_ticket.html",
                  context={"ticket":ticket})