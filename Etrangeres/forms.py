from django.forms import ModelForm
from django import forms
from .models import Etrangere
class EtrangereForm(ModelForm):
    class Meta:
        model =Etrangere
        fields = '__all__'
        widgets = {
            'Nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'prenom ':forms.EmailInput(attrs={'placeholder':'prenom'}),
            'CNI':forms.TextInput(attrs={'placeholder':'matricule'}),
            'telephone':forms.TextInput(attrs={'placeholder':'telephone'}),
        }
        
     