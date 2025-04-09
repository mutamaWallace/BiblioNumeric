from django.urls import path
from .views import *

urlpatterns=[
    path('campuses',all_campuses,name='campuses'),
    path('addcampus',create_campus,name='new_campus'),
    path('update_campus/<int:Id>',update_campus,name='update_campus'),
    path('delete_campus/<int:Id>',delete_campus,name='del_campus'),
]