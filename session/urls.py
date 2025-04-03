from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.conx,name='connexion'),
    # librarian url's 
    path('librarian/',views.librarian,name='librarian'), 
    # publisher url's
    path('publisher/',views.pubisher,name='publisher'), 
    # admin url's
    path('dashbord/',views.dashboard,name='dashbord'), 
    path('register',views.register,name='registration'), 
    path('logout',views.logout,name='logout'),
]