from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context = {
        
    }
    return render(request, "bases/index.html", context)

#traitement de la connexion
def login(request):
    context = {
        
    }
    return render(request, "bases/login.html", context)

#fonction pour le traitement de l'enregistrement
def register(request):
    context = {
        
    }
    return render(request, "bases/register.html", context)


def handle_404(request):
    
    return render(request, "bases/404.html", status=404)