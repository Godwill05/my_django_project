from django import forms
from .models import info
import flet

class Transfert(forms.ModelForm):
    #nom = forms.CharField(max_length=20, min_length=5, empty_value="Ton nom", required=True, label="Nom", help_text="Ton nom")
    #prenom = forms.CharField(max_length=30,min_length=2, empty_value="Prénom", required=True, label="Prénom")
    #photo = forms.ImageField(label="Photo de Profil", required=True)
    
    class Meta:
        model = info
        fields = ('nom', 'prenom', 'photo')
