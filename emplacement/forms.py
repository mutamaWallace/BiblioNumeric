from django.forms import ModelForm
from django import forms
from .models import Emplacement
class EmplacementForm(ModelForm):
    class Meta:
        model =Emplacement
        fields ='__all__'
        widgets = {
            'position_precise': forms.TextInput(attrs={'placeholder': 'precisez le rang de l\ emplacement'}),
             }