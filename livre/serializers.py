from  rest_framework import serializers
from .models import Livre
 
from django import forms
class LivreSerializer(serializers.ModelSerializer):
     class Meta:
         model = Livre
         fields = '__all__'
         widgets = {
            'titre': forms.TextInput(attrs={'placeholder': 'veuillez préciser le titre du livre'}),
        }