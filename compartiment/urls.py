from django.urls import path
from .views import *
urlpatterns=[
    
    path('compart',all_etagere,name='compart'),
    path('create_compart',create_compart,name='create_compart'),
    path('delete_compart/<int:id>',delete_compart,name='delete_compart'),
    path('update_compartiment/<int:id>',update_compartiment,name='update_compartiment'),
]