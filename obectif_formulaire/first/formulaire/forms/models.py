from django.db import models

# Create your models here.

class info(models.Model):
    nom = models.CharField(verbose_name="Nom", max_length=255)
    prenom = models.CharField(verbose_name="Prénom", max_length=255)
    photo = models.ImageField(verbose_name="Photo de profil", upload_to="./img")
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Infos"
        
        
