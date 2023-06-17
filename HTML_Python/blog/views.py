from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from . import forms, models
from authentication.forms import MAJParticipation

@login_required
def creation_ticket(request):
    ticket_form = forms.TicketForm()
    print(request.user.nombre_ticket)
    print(ticket_form)
    if request.method == "POST":
        ticket_form= forms.TicketForm(request.POST, request.FILES)
        print(ticket_form)
        # On vérifie que le formulaire est valide
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.auteur = request.user
            ticket.save()
            return redirect("home")
    context ={"ticket_form": ticket_form}
    return render(request,
                  "blog/creation_ticket.html",
                  context = context)

@login_required
def creation_critique(request):
    critique_form = forms.CritiqueForm()
    utilisateur_form = MAJParticipation()
    print(request.user)
    print(utilisateur_form)
    if request.method == "POST":
        #critique_titre = forms.CritiqueTitre(request.POST)
        critique_form = forms.CritiqueForm(request.POST)
        utilisateur_form = MAJParticipation(request.POST)
        print(utilisateur_form)
        # On vérifie que le formulaire est valide
        if critique_form.is_valid():
            critique = critique_form.save(commit=False) 
            critique.auteur = request.user
            critique.save()
            return redirect("home")
    context = {"critique_form": critique_form}
    return render(request,
                  "blog/creation_critique.html",
                  context = context)
'''
def inscription_page(request):
    form = forms.SignupForm()
    if request.method =="POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            # Sauvegarde de l'utilisateur
            user = form.save()             
@login_required
def creation_critique(request):
    critique_form = forms.CritiqueForm()
    user = 
    print(request.user.nombre_critique )
    if request.method == "POST":
        critique_form = forms.CritiqueForm(request.POST, request.FILES)
        maj_form = forms.MAJPost(request.user)
        # On vérifie que le formulaire est valide
        if critique_form.is_valid():
            critique = critique_form.save(commit=False)
            critique.auteur = request.user
            critique.save()
            nbr_critique = maj_form.save(commit=False)
            nbr_critique.user.nombre_critique = request.user.nombre_critique + 1
            nbr_critique.save()
            return redirect("home")
    context ={"critique_form": critique_form}
    return render(request,
                  "blog/creation_critique.html",
                  context = context)

@login_required
def creation_critique(request):
    critique_form = forms.CritiqueForm()
    if request.method == "POST":
        critique_form = forms.CritiqueForm(request.POST, request.FILES)
        # On vérifie que le formulaire est valide
        if critique_form.is_valid():
            critique = critique_form.save(commit=False)
            critique.auteur = request.user
            critique.save()
            # Mise à jour du nombre de critiques de l'utilisateur
            request.user.nombre_critique += 1
            request.user.save()
            return redirect("home")
    context ={"critique_form": critique_form}
    return render
'''