from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from . import forms, models

@login_required
def creation_ticket(request):
    ticket_form = forms.TicketForm
    illustration_form = forms.IllustrationForm
    if request.method == "POST":
        ticket_form= forms.TicketForm(request.POST)
        illustration_form = forms.IllustrationForm(request.POST, request.FILES)
        # On vérifie que le formulaire est valide
        if all([ticket_form.is_valid(),
                illustration_form.is_valid()]):
            # On sauvegarde l'illustration
            illustration = illustration_form.save(commit=False)
            illustration.auteur = request.user
            illustration.save()
            # On sauvegarde l'illustration avec le ticket
            ticket = ticket_form.save(commit=False)
            ticket.auteur = request.user
            ticket.illustration = illustration
            ticket.save()
            return redirect("home")
    context ={"ticket_form": ticket_form,
              "illustration_form": illustration_form}
    return render(request,
                  "blog/creation_ticket.html",
                  context = context)

@login_required
def creation_critique(request):
    return render(request, "blog/creation_critique.html")