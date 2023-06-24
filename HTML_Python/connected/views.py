from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from . import forms, models

@login_required
def home(request):
    return render(request, "connected/home.html")

@login_required
def page_personnel(request):
    return render(request,"connected/page_personnel.html")


@login_required
def gestion_utilisateur(request):
    utilisateurs = User.objects.all()
    form_utilisateur = forms.ModificationUtilisateur(request.POST)
    
    if request.method == "POST":
        form_utilisateur = forms.ModificationUtilisateur(request.POST)
        print(form_utilisateur)
        
        if form_utilisateur.is_valid():
            utilisateur = form_utilisateur.save(commit=False)
            print (request)
            print (utilisateur)
            utilisateur.role = request.role
            utilisateur.save()
            return redirect("home")
    
    return render(request,
                  "connected/gestion_utilisateur.html",
                  context={"utilisateurs":utilisateurs,
                           "form_utilisateur":form_utilisateur})

