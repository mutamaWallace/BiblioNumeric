from django.db import models
from auteurs.models import *
from etagere.models import *
from compartiment.models import *
from emplacement.models import *
# Create your models here.    
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
    imagelivre = models.ImageField(upload_to='images/', default='path/to/default/image.jpg')
    auteur = models.ForeignKey(Auteurs, on_delete=models.CASCADE)
    etagere = models.ForeignKey(Etagere, on_delete=models.CASCADE)
    compartiment = models.ForeignKey(Compartiment, on_delete=models.CASCADE)
    id_emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.titre} {self.langueLivre} {self.annee_publication} {self.imagelivre} {self.auteur.nom}"
