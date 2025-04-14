from django.db import models
from campus.models import Campus

# Create your models here.

class Pays(models.Model):
    pays = models.CharField(max_length=40)
    def __str__(self):
        return self.pays
class Ville(models.Model):
    ville = models.CharField(max_length=33)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ville
    
class Universite(models.Model):
    universite = models.CharField(max_length=333)
    email_universite = models.EmailField(max_length=33)
    site_web = models.URLField(max_length=33)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    def __str__(self):
        return self.universite
    
class Faculte(models.Model):
    faculte = models.CharField(max_length=33)
    universite = models.ForeignKey(Universite, on_delete=models.CASCADE)
    def __str__(self):
        return self.faculte
class Niveaux(models.Model):
    niveaux_choices = [
        ('BAC1', 'Baccalaureat 1'),
        ('BAC2', 'Baccalaureat 2'),
        ('BAC3', 'Baccalaureat 3'),
        ('1Annee', 'Institut 1'),
        ('2Annee', 'Institut 2'),
        ('3Annee', 'Institut 3'),
    ]
    
    niveau = models.CharField(max_length=7, choices=niveaux_choices)
    faculte = models.ForeignKey(Faculte, on_delete=models.CASCADE)
    def __str__(self):
        return self.niveau
    
class Departement(models.Model):
    departement = models.CharField(max_length=33)
    faculte = models.ForeignKey(Faculte, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    def __str__(self):
        return self.departement
    