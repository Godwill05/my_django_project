from django.db import models

# Create your models here.

class Categories(models.Model):
    
    lib_cat = models.CharField(max_length = 70, unique = True, verbose_name = "Libellé")
    code_cat = models.CharField(max_length = 30, unique = True, verbose_name = "Code Catégorie")
    def __str__(self):
        return self.lib_cat
    
    class Meta():
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"
        
class Autheur(models.Model):
    coor_aut = models.CharField(max_length = 100, unique = True, verbose_name ="Nom Prénom auteur")
    
    
    def __str__(self):
        return self.coor_aut
    
    class Meta():
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        
class LivreBibliotheque(models.Model):
    id_livre = models.IntegerField( unique = True, primary_key = True, verbose_name="id", auto_created=True)
    titre = models.CharField(max_length=255, verbose_name="Titre")
    descriptions = models.CharField(verbose_name = "Description", max_length=255)
    date_sortie = models.DateField(verbose_name="Date de sortie")
    nbr_lecture = models.IntegerField(verbose_name="Nombre de lecture au total")
    auteur = models.ForeignKey(Autheur, on_delete=models.DO_NOTHING, verbose_name="Autheur")
    catego = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, verbose_name="Categorie")
    def __str__(self):
        return self.titre
    
    class Meta():
        verbose_name="Livre"
        verbose_name_plural="Livres"
    