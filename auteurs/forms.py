from django.forms import ModelForm
from django import forms
from .models import Auteurs
class AuteursForm(ModelForm):
    class Meta:
        model =Auteurs
        fields ='__all__'
        widgets = {
            'Nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'Prenom':forms.TextInput(attrs={'placeholder':'Telephone'}),
            'Postnom':forms.TextInput(attrs={'placeholder':'postnom'}),
            'CNI':forms.TextInput(attrs={'placeholder':'CNI'}),
            'Email':forms.TextInput(attrs={'placeholder':'Email'}),
        }