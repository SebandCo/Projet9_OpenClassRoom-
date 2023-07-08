from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required
from authentication.models import User
from . import forms
from blog.models import Ticket, Critique


@login_required
def page_personnel(request):
    tickets = Ticket.objects.all()
    critiques = Critique.objects.all()
    mes_tickets = []
    mes_critiques = []
    for ticket in tickets:
        if ticket.auteur == request.user:
            mes_tickets.append(ticket)

    for critique in critiques:
        if critique.auteur == request.user:
            mes_critiques.append(critique)

    return render(request,
                  "connected/page_personnel.html",
                  context={"tickets": mes_tickets,
                           "critiques": mes_critiques})


@login_required
# @permission_required ("gestion_utilisateur", raise_exception=True)
def gestion_utilisateur(request):
    utilisateurs = User.objects.all()
    utilisateur = User(request)
    form_utilisateur = forms.ModificationUtilisateur()
    if request.method == "POST":
        # Récupére la liste des roles de la méthode POST
        liste_role = request.POST.getlist('role')
        rang = 0
        if request.user.role == "Administrateur":
            for utilisateur in utilisateurs:
                # Ne modifie que les autres utilisateurs
                if utilisateur != request.user:
                    # Affecte les roles suivant la liste des utilisateurs
                    utilisateur.role = liste_role[rang]
                    utilisateur.save()
                    rang += 1
        else:
            return redirect("home")

    return render(request,
                  "connected/gestion_utilisateur.html",
                  context={"utilisateurs": utilisateurs,
                           "form_utilisateur": form_utilisateur})


@login_required
def home(request):
    # Tri des tickets et critiques par ordre décroissant de création
    # Donc du plus rescent ou plus ancien
    # N'affiche que les 5 premieres réponses
    tickets = Ticket.objects.all().order_by("-date_creation")[:5]
    critiques = Critique.objects.all().order_by("-date_creation")[:5]
    return render(request,
                  "connected/home.html",
                  context={"tickets": tickets,
                           "critiques": critiques})


@login_required
def abonnement_utilisateur(request):
    utilisateurs = User.objects.all()
    abonnements = request.user.abonnement.all()
    # Regarde si c'est une méthode POST
    if request.method == "POST":
        # si le bouton est "suivre" on rajoute à la base de donnée
        if request.POST.get("suivre"):
            request.user.abonnement.add(request.POST.get("suivre"))
        # Si le bouton est "ne plus suivre" on enleve de la base de donnée
        elif request.POST.get("ne_plus_suivre"):
            request.user.abonnement.remove(request.POST.get("ne_plus_suivre"))
    return render(request,
                  "connected/abonnement_utilisateur.html",
                  context={"utilisateurs": utilisateurs,
                           "abonnements": abonnements})


def follow_user(request):
    follow_user = User.objects.get(pk=request.user.id)

    if request.method == "POST":
        current_user_profile = request.user
        action = request.POST['follow']
        if action == "unfollow":
            current_user_profile.follows.remove(follow_user)
        elif action == "follow":
            current_user_profile.follows.add(follow_user)

    return render(request,
                  'connected/newuser_detail.html',
                  {"follow_user": follow_user})
