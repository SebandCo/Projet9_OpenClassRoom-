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
    path("blog/creation_critique/", blog.views.creation_critique, name="creation_critique"),
]
