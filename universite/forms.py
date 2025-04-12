from django.forms import ModelForm
from django import forms
from .models import Universite, Faculte, Departement, Niveaux, Pays, Ville
class UniversiteForm(ModelForm):
    class Meta:
        model =Universite
        fields ='__all__'
        widgets = {
            'Nom de l universite': forms.TextInput(attrs={'placeholder': 'Nom de l universite'}),
            'email':forms.EmailInput(attrs={'placeholder':'email de l universite'}),
            'site_web':forms.TextInput(attrs={'placeholder':'site web de l universite'}),
        }
        
        
class FaculteForm(ModelForm):
    class Meta:
        model =Faculte
        fields ='__all__'
        widgets = {
            'Nom de la faculte': forms.TextInput(attrs={'placeholder': 'Nom de la faculte'}),
          
        }
        
class DepartimentForm(ModelForm):
    class Meta:
        model =Departement
        fields ='__all__'
        widgets = {
            'Nom du departiment': forms.TextInput(attrs={'placeholder': 'Nom du departement'}),
          
        }


class NiveauxForm(ModelForm):
    class Meta:
        model =Niveaux
        fields ='__all__'
       
        
class VilleForm(ModelForm):
    class Meta:
        model =Ville
        fields ='__all__'
        widgets = {
            'Ville': forms.TextInput(attrs={'placeholder': 'ville'}),
          
        }
        
class PaysForm(ModelForm):
    class Meta:
        model =Pays
        fields ='__all__'
        widgets = {
            'pays': forms.TextInput(attrs={'placeholder': 'pays'}),
          
        }