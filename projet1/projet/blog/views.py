from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

def index(request):
    
    context = {
        "message":"valeur",
        
    }
    template = loader.get_template("blog/index.html")
    return HttpResponse(template.render(context, request))
# Create your views here.
