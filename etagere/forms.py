from django.forms import ModelForm
from django import forms
from .models import Etagere
class EtagereForm(ModelForm):
    class Meta:
        model =Etagere
        fields ='__all__'
        widgets = {
            'Nom': forms.TextInput(attrs={'placeholder': 'Nom de l\ etagere'}),
            'etat_etagere':forms.TextInput(attrs={'placeholder':'etat de l\ etagere'}),
            'charge_maximal':forms.TextInput(attrs={'placeholder':'veuillez precisez la taille maximale'}),
        }