from django.forms import ModelForm
from django import forms
from .models import Compartiment
class CompartimentForm(ModelForm):
    class Meta:
        model =Compartiment
        fields ='__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'nom du compartiment'}),
            'nombreLivre':forms.TextInput(attrs={'placeholder':'nombre de livre percu par le compartiment'}),
            'domaineLivre':forms.TextInput(attrs={'placeholder':'veuillez precisez le domaine des livres'}),
        }