from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
#from django.template import loader
from .models import Book, Author
# Create your views here.

from .forms import SomeForm

def index(request):
    #return HttpResponse("<p style=color:red;>Bienvenue sur Managlib ! </p><br>")
    
    
    if request.method == 'POST':
        form = SomeForm(request.POST)
        if form.is_valid():
            return redirect("mangalib:index")
        
    else:
        form = SomeForm()
     
    
    #template = loader.get_template("mangalib/index.html")
    context = {
        "message":"Hello world",
        "newscontent": 15,
        "users":["Vincent", "Laurent", "Jean", "Isaac"],
        "books" : Book.objects.all().order_by("title") ,
        "form" : form
        }
    return render(request, "mangalib/index.html", context)

def show(request, book_id):
    context = {
        "book" : get_object_or_404(Book, pk=book_id)
    }
    
    return render(request,  "mangalib/book.html", context)

def add(request):
    author = Author.objects.get(name = "Akira Toriyama")
    book = Book.objects.create(title = "Dragon Quest", quantity=13, author=author)
    return redirect("mangalib:index")
