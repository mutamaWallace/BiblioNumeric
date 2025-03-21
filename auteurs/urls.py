from django.urls import path
from .views import *

urlpatterns=[
    path('all_authors',all_authors,name='all_Authors'),
    path('add_author', new_author,name='new_author'),
    path('update_author/<int:Id>',update_Author,name='update_author'),
    path('delete_author/<int:Id>',delete_Author,name='del_author'),
]