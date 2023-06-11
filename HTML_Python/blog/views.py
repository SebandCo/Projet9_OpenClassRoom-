from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from . import forms, models

@login_required
def creation_ticket(request):
    ticket_form = forms.TicketForm
    image_form = forms.ImageForm
    if request.method == "POST":
        ticket_form= forms.TicketForm(request.POST)
        image_form = forms.ImageForm(request.POST, request.FILES)
        # On vérifie que le formulaire est valide
        if all([ticket_form.is_valid(),
                image_form.is_valid()]):
            # On sauvegarde la image
            image = image_form.save(commit=False)
            image.auteur = request.user
            image.save()
            # On sauvegarde l'image avec le ticket
            ticket = ticket_form.save(commit=False)
            ticket.auteur = request.user
            ticket.image = image
            ticket.save()
            return redirect("home")
    context ={"ticket_form": ticket_form,
              "image_form": image_form}
    return render(request,
                  "blog/creation_ticket.html",
                  context = context)

@login_required
def creation_critique(request):
    return render(request, "blog/creation_critique.html")