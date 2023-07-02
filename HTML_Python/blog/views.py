from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.shortcuts import get_object_or_404

# ------------- Gestion des critiques ----------------
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
                  context = {"critique_form": critique_form})

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
                  context = {"critique_form": critique_form,
                             "ticket":ticket})

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
            else:
                return redirect("home")
    return render(request,
                  "blog/modification_ticket.html",
                  context = {"ticket_form": ticket_form})

@login_required
def affichage_des_tickets(request):
    tickets = models.Ticket.objects.all()
    return render(request,
                  "blog/affichage_des_tickets.html",
                  context={"tickets":tickets})

@login_required
def affichage_dun_ticket(request, ticket_id):
    ticket_choisi = get_object_or_404(models.Ticket, id=ticket_id)
    critiques = models.Critique.objects.filter(ticket=ticket_choisi)
    print(critiques)
    return render(request,
                  "blog/affichage_dun_ticket.html",
                  context={"ticket":ticket_choisi,
                           "critiques":critiques})