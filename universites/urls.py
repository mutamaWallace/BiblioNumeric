from django.urls import path
from .views import *

urlpatterns=[
    path('universities',all_universities,name='universities'),
    path('adduniversite',create_universite,name='new_universit'),
    path('update_universite/<int:pk>',update_universite,name='update_universite'),
    path('delete_universite/<int:Id>',delete_universite,name='del_univer'),
    path('faculties',all_faculties,name='faculties'),
    path('addfaculte',create_faculte,name='new_faculte'),
    path('update_faculte/<int:pk>',update_faculte,name='update_faculte'),
    path('delete_faculte/<int:Id>',delete_faculte,name='del_facult'),
    path('departements',all_departements,name='departements'),
    path('adddepartement',create_departement,name='new_departement'),
    path('update_departement/<int:pk>',update_departement,name='update_departement'),
    path('delete_departement/<int:Id>',delete_departement,name='del_depart'),
    path('niveaux',all_classes,name='niveaux'),
    path('addclass',create_class,name='new_class'),
    path('update_class/<int:pk>',update_class,name='update_class'),
    path('delete_class/<int:Id>',delete_class,name='del_class'),
]