from django.forms import ModelForm
from django import forms
from .models import Etudiants
class EtudiantsForm(ModelForm):
    class Meta:
        model =Etudiants
        fields = ['nom','prenom','genre','matricule','domicile','date_emprunt','date_fin_emprunt','universite', 'faculte','niveau','livre']
        widgets = {
            'Nom de l etudiant': forms.TextInput(attrs={'placeholder': 'Nom de l étudiant'}),
            'prenom de l etudiant ':forms.EmailInput(attrs={'placeholder':'prenom de l étudiant'}),
            'matricule de l etudiant':forms.TextInput(attrs={'placeholder':'matricule de l étudiant'}),
            'domicile de l etudiant':forms.TextInput(attrs={'placeholder':'domicile de l étudiant'}),
        }
        
     