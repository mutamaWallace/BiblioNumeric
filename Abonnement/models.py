from django.db import models
import datetime
# Create your models here.
class Abonnement(models.Model):
    type_abonnement = models.CharField(max_length=30)
    prix = models.FloatField(max_length=30, default=15000)
    date_debut = models.DateField(default=datetime.date.today)
    date_fin = models.DateField(null=True)
    
    def __str__(self):
        return self.type_abonnement
    
