"""
URL configuration for LITReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import blog.views
import connected.views

urlpatterns = [
    path("admin/", admin.site.urls),
    # URL d'authentification
    path("", authentication.views.login_page, name='login'),
    path("logout/", authentication.views.logout_page, name="logout"),
    # URL de connexion
    path("home/", connected.views.home, name="home"),
    # URL d'inscription
    path("inscription/", authentication.views.inscription_page, name="inscription"),
    # URL page personnel
    path("home/page_personnel/", connected.views.page_personnel, name="page_personnel"),
    # URL création de ticket et critique
    path("blog/creation_ticket/", blog.views.creation_ticket, name="creation_ticket"),
    path("blog/creation_critique_vide/", blog.views.creation_critique_vide, name="creation_critique_vide"),
    path("blog/creation_critique_liee/<int:ticket_id>/", blog.views.creation_critique_liee, name="creation_critique_liee"),
    # URL affichage des tickets
    path("blog/affichage_des_tickets/", blog.views.affichage_des_tickets, name="affichage_des_tickets"),
    path("blog/affichage_dun_ticket/<int:ticket_id>/", blog.views.affichage_dun_ticket, name="affichage_dun_ticket"),
    # URL modification des tickets/critiques
    path("blog/modification_critique/<int:critique_id>/", blog.views.modification_critique, name="modification_critique"),
    path("blog/modification_ticket/<int:ticket_id>/", blog.views.modification_ticket, name="modification_ticket"),
    # URL suppression des tickets/critiques
    path("blog/suppression_critique/<int:critique_id>/", blog.views.suppression_critique, name="suppression_critique"),
    path("blog/suppression_ticket/<int:ticket_id>/", blog.views.suppression_ticket, name="suppression_ticket"),
    # URL gestion des utilisateurs
    path("connected/gestion_utilisateur/", connected.views.gestion_utilisateur, name="gestion_utilisateur"),
    # URL abonnement utilisateur
    path("connected/abonnement_utilisateur/", connected.views.abonnement_utilisateur, name="abonnement_utilisateur"),
    path("connected/follow_user/", connected.views.follow_user, name="follow_user")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
