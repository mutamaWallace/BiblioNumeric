from django.forms import ModelForm
from django import forms
from .models import Emprunt
class EmpruntForm(ModelForm):
    class Meta:
        model =Emprunt
        fields = '__all__'
        widgets = {
            'date_debut': forms.DateInput(attrs={
                'placeholder':'Date début emprunt',
                'type':'date'
            }),
             'date_fin_emprunt': forms.DateInput(attrs={
                'placeholder':'Date fin emprunt',
                'type':'date'
            }),    
        }



     