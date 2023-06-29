from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from . import forms, models
from blog.models import Ticket, Critique


@login_required
def page_personnel(request):
    tickets = Ticket.objects.all()
    critiques = Critique.objects.all()
    mes_tickets = []
    for ticket in tickets:
        if ticket.auteur == request.user :
            mes_tickets.append(ticket)

    return render(request,
                  "connected/page_personnel.html",
                  context={"tickets":mes_tickets,
                           "critiques":critiques})


@login_required
def gestion_utilisateur(request):
    utilisateurs = User.objects.all()
    utilisateur = User(request)
    form_utilisateur = forms.ModificationUtilisateur()
    if request.method == "POST":
        # Récupére la liste des roles de la méthode POST
        liste_role=request.POST.getlist('role')
        rang=0
        for utilisateur in utilisateurs:
            # Ne modifie que les autres utilisateurs
            if utilisateur != request.user:
                # Affecte les roles suivant la liste des utilisateurs
                utilisateur.role = liste_role[rang]
                utilisateur.save()
                rang += 1
    
    return render(request,
                  "connected/gestion_utilisateur.html",
                  context={"utilisateurs":utilisateurs,
                           "form_utilisateur":form_utilisateur})

@login_required
def home(request):
    # Tri des tickets et critiques par ordre décroissant de création
    # Donc du plus rescent ou plus ancien
    # N'affiche que les 5 premieres réponses
    tickets = Ticket.objects.all().order_by("-date_creation")[:5]
    critiques = Critique.objects.all().order_by("-date_creation")[:5]
    return render(request,
                  "connected/home.html",
                  context={"tickets":tickets,
                           "critiques":critiques})

@login_required
def abonnement_utilisateur(request):
    utilisateurs = User.objects.all()
    follower_form = forms.FollowerForm(instance = request.user)
    if request.method == "POST":
        follower_form = forms.FollowerForm(request.POST, instance = request.user)
        if follower_form.is_valid():
            follower_form.save()
            return redirect("home")
    return render(request,
                  "connected/abonnement_utilisateur.html",
                  context={"utilisateurs":utilisateurs,
                           "follower_form":follower_form})
