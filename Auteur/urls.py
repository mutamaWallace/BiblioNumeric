from django.urls import path
from .views import allauthors,create_author,update_author,delete_author

urlpatterns=[
    path('authors',allauthors,name='authors'),
    path('addauthor',create_author,name='new_author'),
    path('update_author/<int:Id>',update_author,name='update_author'),
    path('delete_author/<int:Id>',delete_author,name='del_author'),
]