from django.forms import ModelForm
from django import forms
from .models import Campus
class CampusForm(ModelForm):
    class Meta:
        model =Campus
        fields ='__all__'
        widgets = {
            'code_campus': forms.TextInput(attrs={'placeholder': 'veuillez saisir le code du campus'}),
            'campus':forms.TextInput(attrs={'placeholder':'veuillez saisir le campus'}),
            
        }