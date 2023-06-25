from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from . import forms, models
from blog.models import Ticket, Critique

@login_required
def home(request):
    return render(request,
                  "connected/home.html")

@login_required
def page_personnel(request):
    return render(request,
                  "connected/page_personnel.html")


@login_required
def gestion_utilisateur(request):
    utilisateurs = User.objects.all()
    form_utilisateur = forms.ModificationUtilisateur()
    if request.method == "POST":
        # Récupére la liste des roles de la méthode POST
        liste_role=request.POST.getlist('role')
        rang=0
        for utilisateur in utilisateurs:
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
    print(tickets)
    return render(request,
                  "connected/home.html",
                  context={"tickets":tickets,
                           "critiques":critiques})