from django.db import models
from Abonnement.models import Abonnement
# Create your models here.


class Etrangere(models.Model):
    GENRE_CHOICES = [
        ('A', 'Autres'),
        ('F', 'Feminin'),
        ('M', 'Masculin'),
        # Add more choices as needed
    ]
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    genre = models.CharField(max_length=1, choices= GENRE_CHOICES)
    CNI = models.CharField(max_length=20)
    telephone = models.CharField(max_length=30)
    abonnement = models.ForeignKey(Abonnement, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nom 