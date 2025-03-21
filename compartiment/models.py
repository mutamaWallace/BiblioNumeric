from django.db import models
from etagere.models import *

# Create your models here.


class Compartiment(models.Model):
    nom = models.CharField(max_length=100)
    nombreLivre = models.IntegerField()
    domaineLivre = models.CharField(max_length=255, default='francais')
    etagere = models.ForeignKey(Etagere, on_delete=models.CASCADE)

    def __str__(self):
        return self.domaineLivre