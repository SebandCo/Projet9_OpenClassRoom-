from django.shortcuts import render, redirect
from . import forms
# import des fonctions d'authentification
from django.contrib.auth import login, authenticate
# import des fonctions de deconnexion
from django.contrib.auth import logout
# import du fichier settings
from django.conf import settings


def inscription_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            # Sauvegarde de l'utilisateur
            user = form.save()
            # Connexion automatique de l'utilisateur
            login(request, user)
            # Redirection en utilisant le chemin LOGIN_REDIRECT_URL
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,
                  'authentication/inscription.html',
                  context={'form': form})


def logout_page(request):
    # Fonction de deconnextion
    logout(request)
    # Retour vers la page de login
    return redirect('login')


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # Appel de la fonction authenticate
            user = authenticate(
                # Récupére les données puis les efface
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            # Si l'utilisateur existe
            if user is not None:
                login(request, user)
                return redirect("home")
            # Sinon
            else:
                message = 'Identifiants invalides.'

    return render(request,
                  'authentication/connexion.html',
                  context={'form': form, 'message': message})
