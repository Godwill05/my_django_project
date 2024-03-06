from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Categories, LivreBibliotheque, Autheur
# Create your views here.

def index(request):
    context = {
        "name":"valeur",
        
    }
    
    return render(request, "bibliotheque/index.html", context)

def bibliotheque(request):
    context = {
        "recup":LivreBibliotheque.objects.all(),
    }
    return render(request, "bibliotheque/bibi.html", context)

def livre(request, id):
    context = {
        "livre":get_object_or_404(LivreBibliotheque, pk=id)
    }
    
    return render(request, "bibliotheque/livre.html", context)