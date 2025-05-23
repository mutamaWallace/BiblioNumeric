"""magazin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 


from rest_framework import routers
from livreAPI.urls import router as livre_router



router = routers.DefaultRouter()
router.registry.extend(livre_router.registry)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('product.urls')),
    path('',include('session.urls')),
    path('',include('Auteur.urls')),
    path('',include('Fournisseur.urls')),
    path('',include('parametre.urls')),
    path('',include('etagere.urls')),
    path('',include('compartiment.urls')),
    path('',include('emplacement.urls')),
    path('',include('livre.urls')),
    path('',include('auteurs.urls')),
    path('',include('campus.urls')),
    path('',include('universite.urls')),
    path('',include('etudiants.urls')),
    path('',include('bibliothecaires.urls')),
    path('',include('Abonnement.urls')),
    path('',include('Etrangeres.urls')),
     path('',include('emprunts.urls')),
     path('', include(router.urls),)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)