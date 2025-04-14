from django.urls import path
from .views import *

urlpatterns=[
    path('abonnes',all_abonnements,name='abonnes'),
    path('addabonnes',create_abonnee,name='new_abonnes'),
    path('update_abonne/<int:pk>',update_abonne,name='update_abonne'),
    path('delete_abonne/<int:Id>',delete_abonne,name='del_abonne'),
]