from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "connected/home.html")

@login_required
def page_personnel(request):
    return render(request,"connected/page_personnel.html")