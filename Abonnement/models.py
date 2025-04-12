from django.db import models

# Create your models here.
class Abonnement(models.Model):
    type_abonnement = models.CharField(max_length=30)
    date_debut = models.DateField
    date_fin = models.DateField
    
    def __str__(self):
        return self.type_abonnement
    
