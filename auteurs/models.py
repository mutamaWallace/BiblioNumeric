from django.db import models

# Create your models here.

class Auteurs(models.Model):
    Id=models.AutoField(primary_key=1)
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    postnom = models.CharField(max_length=30)
    CNI=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    def _str_(self):
       return self.nom
