from django.db import models
import datetime
from Etrangeres.models import Etrangere
from livre.models import Livre
from etudiants.models import Etudiants
# Create your models here.
class Emprunt(models.Model):
    date_debut = models.DateField(default=datetime.date.today)
    date_fin_emprunt = models.DateField(null=True)
    livre = models.ForeignKey(Livre, on_delete=models.PROTECT)
    etrangere = models.ForeignKey(Etrangere, on_delete=models.PROTECT)
    # etudiant = models.ForeignKey(Etudiants, on_delete=models.PROTECT)
    rendu = models.BooleanField(default=False)
    