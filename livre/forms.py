from django.forms import ModelForm
from django import forms
from django.core.validators import MinValueValidator
from .models import Livre
class LivreForm(ModelForm):
    annee_publication = forms.IntegerField(
        validators=[MinValueValidator(1000)],  # Assurez-vous que l'année est positive
        widget=forms.TextInput(attrs={'placeholder': 'année de publication'})
    )
    
    class Meta:
        model = Livre
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'placeholder': 'veuillez préciser le titre du livre'}),
        }