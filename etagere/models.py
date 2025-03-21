from django.db import models

# Create your models here.
   
class Etagere(models.Model):
    
    nom = models.CharField(max_length=100)
    etat_etagere = models.CharField(max_length=50)
    mobilite = models.BooleanField(default=False)
    charge_maximal = models.PositiveIntegerField()
    def __str__(self):
        return self.nom
