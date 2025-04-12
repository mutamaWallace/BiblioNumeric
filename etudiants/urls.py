from django.urls import path
from .views import *

urlpatterns=[
    path('etudiants',all_students,name='etudiants'),
    path('add_student',emprunt_book_to_student,name='new_student'),
    path('update_student/<int:pk>',update_student,name='update_student'),
    #path('delete_student/<int:Id>',delete_stu,name='del_student'),
]
