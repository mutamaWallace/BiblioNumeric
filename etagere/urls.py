from django.urls import path
from .views import *

urlpatterns=[
    path('etageres',all_etagere,name='etageres'),
    path('addetagere',create_etagere,name='new_etagere'),
    path('update_etagere/<int:Id>',update_etagere,name='update_etagere'),
    path('delete_etagere/<int:Id>',delete_etagere,name='del_etagere'),
]