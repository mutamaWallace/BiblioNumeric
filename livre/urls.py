from django.urls import path
from .views import *

urlpatterns=[
    path('livres',all_book,name='livres'),
    path('allbooks/', tous_livres, name = 'allbooks'),
    path('add_book',create_livre,name='new_book'),
    path('update_book/<int:pk>',update_book,name='update_book'),
    path('delete_book/<int:Id>',delete_livre,name='del_book'),
]