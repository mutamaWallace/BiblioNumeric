from django.db import models
from universite.models import Universite
from livre.models import Livre
# from session.models import Utilisateur
import datetime
# Create your models here.


class Bibliothecaire(models.Model):
    gender_choices = [
        ('F','Feminin'),
        ('M','Masculin'),
        ('Au','Autres'),
    ]
    nom = models.CharField(max_length=222)
    prenom = models.CharField(max_length=222)
    genre = models.CharField(max_length=2, choices=gender_choices)
    matricule = models.CharField(max_length=220)
    domicile = models.CharField(max_length=300)
    telephone = models.CharField(max_length=25)
    date_emprunt = models.DateField(default=datetime.date.today)
    date_fin_emprunt = models.DateField(null=True)
    universite = models.ForeignKey(Universite, on_delete=models.PROTECT)
    livre = models.ForeignKey(Livre, on_delete=models.PROTECT)
    rendu = models.BooleanField(default= False)
    