from django.forms import ModelForm
from django import forms
from .models import Bibliothecaire
class BibliothecaireForm(ModelForm):
    class Meta:
        model =Bibliothecaire
        fields = '__all__'
        widgets = {
            'Nom du bibliothecaire': forms.TextInput(attrs={'placeholder': 'Nom de l étudiant'}),
            'prenom du bibliothecaire ':forms.EmailInput(attrs={'placeholder':'prenom de l étudiant'}),
            'matricule du bibliothecaire':forms.TextInput(attrs={'placeholder':'matricule de l étudiant'}),
            'Telephone du bibliothecaire':forms.TextInput(attrs={'placeholder':'Telephone de l étudiant'}),
            
        
        }
        
     