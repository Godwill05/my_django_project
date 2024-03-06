from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import info
from .forms import Transfert

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        formulaire = Transfert(request.POST, request.FILES)
        if formulaire.is_valid():
            formulaire.save()
            HttpResponse("Message")
            return redirect("forms:index")
    else : 
        formulaire = Transfert
    context = {
        "form": formulaire, 
        "recup":info.objects.all()
        
    }
    
    return render(request, "forms/index.html", context)