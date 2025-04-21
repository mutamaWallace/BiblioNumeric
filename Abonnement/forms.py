from django.forms import ModelForm
from django import forms
from .models import Abonnement
class AbonnementForm(ModelForm):
    class Meta:
        model =Abonnement
        fields = '__all__'
        widgets = {
            'Type d abonnement': forms.TextInput(attrs={'placeholder': 'type abonnement'}),
            'Prix':forms.EmailInput(attrs={'placeholder':'prix d un seul abonnnement'}),
        
           'date_debut': forms.DateInput(attrs={
                'placeholder':'Date début abonnement',
                'type':'date'
            }),
             
              'date_fin': forms.DateInput(attrs={
                'placeholder':'Date fin abonnement',
                'type':'date'
            }),
        
        }
        
     