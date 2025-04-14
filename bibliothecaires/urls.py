from django.urls import path
from .views import *

urlpatterns=[
    path('librarians',all_librarians,name='librarians'),
    path('add_librarian',emprunt_book_to_librarian,name='new_librarian'),
    path('update_librarian/<int:pk>',update_librarian,name='update_librarian'),
    #path('delete_student/<int:Id>',delete_stu,name='del_student'),
]
