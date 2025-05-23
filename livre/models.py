from django.db import models
from auteurs.models import *
from etagere.models import *
from compartiment.models import *
from emplacement.models import *
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# Create your models here.  



    
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    
    class Meta:
        swappable ='AUTH_USER_MODEL'
      
class Livre(models.Model):
    LANGUE_CHOICES = [
        ('FR', 'Français'),
        ('EN', 'Anglais'),
        ('ES', 'Espagnol'),
        ('DE', 'Allemand'),
        # Ajoutez d'autres langues si nécessaire
    ]
    
    titre = models.CharField(max_length=200)
    langueLivre = models.CharField(max_length=2, choices=LANGUE_CHOICES)
    annee_publication = models.PositiveIntegerField()
    imagelivre = models.ImageField(upload_to='images/')
    auteur = models.ForeignKey(Auteurs, on_delete=models.CASCADE)
    etagere = models.ForeignKey(Etagere, on_delete=models.CASCADE)
    compartiment = models.ForeignKey(Compartiment, on_delete=models.CASCADE)
    id_emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
