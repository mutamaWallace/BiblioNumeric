from django.db import models
from compartiment.models import *
from etagere.models import *

# Create your models here.


class Emplacement(models.Model):
    position_precise = models.CharField(max_length=30)
    disponibilite = models.BooleanField(default=False)
    id_compartiment = models.ForeignKey(Compartiment, on_delete=models.CASCADE)
    id_etagere = models.ForeignKey(Etagere, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.position_precise
