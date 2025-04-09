from django.forms import ModelForm
from django import forms
from .models import Universite, Faculte, Departement, Class
class UniversiteForm(ModelForm):
    class Meta:
        model =Universite
        fields ='__all__'
        widgets = {
            'Nom de l\ universite': forms.TextInput(attrs={'placeholder': 'Nom de l\ universite'}),
            'email':forms.EmailInput(attrs={'placeholder':'email de l\ universite'}),
            'site_web':forms.TextInput(attrs={'placeholder':'site web de l\ universite'}),
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


class ClassForm(ModelForm):
    class Meta:
        model =Class
        fields ='__all__'
        widgets = {
            'Niveau': forms.TextInput(attrs={'placeholder': 'Niveau'}),
          
        }