from django.contrib import admin

# Register your models here.
from .models import Categories, LivreBibliotheque, Autheur

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'code_cat', 'lib_cat')
    
@admin.register(Autheur)
class AuteurAdmin (admin.ModelAdmin):
    list_display = ('id', 'coor_aut')

@admin.register(LivreBibliotheque)
class LivreBibliothequeAdmin(admin.ModelAdmin):
    list_display = ('id_livre', 'titre', 'descriptions', 'date_sortie', 'nbr_lecture', 'auteur_id', 'catego_id')