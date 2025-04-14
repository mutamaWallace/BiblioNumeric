from django.urls import path
from .views import *

urlpatterns=[
    path('etrangeres',tous_etrangeres,name='etrangeres'),
    path('add_etrangere',create_etrangere,name='new_personne'),
    path('update_etrangere/<int:pk>',update_etrangere,name='update_etrangere'),
    #path('delete_student/<int:Id>',delete_stu,name='del_student'),
]
