from django.urls import path
from .views import *
urlpatterns=[
    
    path('emplacements',all_etagere,name='emplacements'),
    path('create_emplacement/',create_emplacement,name='create_emplacement'),
    path('delete_etager/<int:id>',delete_etager,name='delete_etager'),
    path('update_compartimen/<int:id>',update_compartimen,name='update_compartimen'),
]