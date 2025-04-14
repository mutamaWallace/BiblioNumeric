from django.forms import ModelForm
from django import forms
from .models import Emprunt
class EmpruntForm(ModelForm):
    class Meta:
        model =Emprunt
        fields = '__all__'
        widgets = {
            'date_debut': forms.TextInput(attrs={'placeholder': 'date debut emprunt'}),
            'date_fin ':forms.EmailInput(attrs={'placeholder':'date fin emprunt'}),
        
        }
        
     