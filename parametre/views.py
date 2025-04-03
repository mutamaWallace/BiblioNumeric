from importlib.resources import path
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class deleteaccount(SuccessMessageMixin,generic.DeleteView):
    model=User
    template_name='parametre/delaccount.html'
    success_message="account has been deleted"
    success_url=reverse_lazy("connexion")


class password(SuccessMessageMixin,generic.UpdateView):
    model=User
    template_name='parametre/password.html'
    fields = ['password'] 
    
    def get_object(self, queryset=None):
        return self.request.user
    success_url=reverse_lazy("connexion")




 