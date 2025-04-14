from django.urls import path
from .views import *

urlpatterns=[
    path('emprunts',all_emprunts,name='emprunts'),
    path('add_emprunt',add_emprunt,name='new_emprunt'),
    path('update_emprunt/<int:pk>',update_emprunt,name='update_emprunt'),
    #path('delete_student/<int:Id>',delete_stu,name='del_student'),
]
